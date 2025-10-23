"""
C Code Generator for Minipar Language
Translates Three-Address Code (TAC) to C code
"""

from typing import List, Dict, Set, Optional
try:
    from src.codegen import TAC, CodeGenerator
except ImportError:
    from codegen import TAC, CodeGenerator


class CCodeGenerator:
    """Generates C code from Three-Address Code"""
    
    def __init__(self):
        self.c_code: List[str] = []
        self.functions: Dict[str, List[str]] = {}
        self.current_function: Optional[str] = None
        self.function_code: List[str] = []
        self.indent_level = 0
        self.temp_vars: Set[str] = set()
        self.global_vars: Dict[str, str] = {}
        self.function_signatures: Dict[str, tuple] = {}
        self.function_params: Dict[str, List[str]] = {}
        self.label_map: Dict[str, str] = {}
        self.in_par_block = False
        self.par_thread_funcs: List[str] = []
        self.par_thread_code: Dict[int, List[str]] = {}
        self.current_thread_id: Optional[int] = None
        self.pending_params: List[str] = []
        self.last_label: Optional[str] = None
    
    def indent(self) -> str:
        """Get current indentation"""
        return "    " * self.indent_level
    
    def emit(self, line: str):
        """Emit a line of C code"""
        if self.current_function:
            self.function_code.append(self.indent() + line)
        else:
            self.c_code.append(self.indent() + line)
    
    def emit_blank(self):
        """Emit a blank line"""
        if self.current_function:
            self.function_code.append("")
        else:
            self.c_code.append("")
    
    def generate(self, tac_instructions: List[TAC]) -> str:
        """
        Generate C code from TAC instructions
        Returns the complete C program as a string
        """
        # Reset state
        self.c_code = []
        self.functions = {}
        self.temp_vars = set()
        self.global_vars = {}
        self.function_signatures = {}
        
        # First pass: collect information about functions and variables
        self._analyze_tac(tac_instructions)
        
        # Generate C code
        self._generate_headers()
        self._generate_forward_declarations()
        self._generate_global_variables()
        self._generate_functions(tac_instructions)
        self._generate_main_function(tac_instructions)
        
        return "\n".join(self.c_code)
    
    def _analyze_tac(self, instructions: List[TAC]):
        """First pass: analyze TAC to collect information"""
        current_func = None
        
        for i, instr in enumerate(instructions):
            if instr.op == 'FUNC_BEGIN':
                current_func = instr.arg1
                # Collect function parameters
                params = []
                j = i + 1
                while j < len(instructions) and instructions[j].op == 'PARAM':
                    params.append(instructions[j].arg1)
                    j += 1
                self.function_params[current_func] = params
            elif instr.op == 'FUNC_END':
                current_func = None
            elif current_func is None:
                # Global scope - collect global variables
                if instr.op == 'ASSIGN' and instr.result and not instr.result.startswith('t'):
                    self.global_vars[instr.result] = 'int'  # Default to int
            
            # Collect temporary variables
            if instr.result and instr.result.startswith('t'):
                self.temp_vars.add(instr.result)
    
    def _generate_headers(self):
        """Generate C headers and includes"""
        self.emit("#include <stdio.h>")
        self.emit("#include <stdlib.h>")
        self.emit("#include <string.h>")
        self.emit("#include <stdbool.h>")
        
        # Add pthread if we have PAR blocks
        if any(instr.op in ['PAR_BEGIN', 'THREAD_START'] for instr in []):
            self.emit("#include <pthread.h>")
        
        self.emit_blank()
    
    def _generate_forward_declarations(self):
        """Generate forward declarations for functions"""
        if self.function_params:
            self.emit("// Forward declarations")
            for func_name, params in self.function_params.items():
                param_list = ", ".join([f"int {p}" for p in params])
                self.emit(f"int {func_name}({param_list});")
            self.emit_blank()
    
    def _generate_global_variables(self):
        """Generate global variable declarations"""
        if self.global_vars:
            self.emit("// Global variables")
            for var_name, var_type in self.global_vars.items():
                self.emit(f"int {var_name};  // Global variable")
            self.emit_blank()
    
    def _generate_functions(self, instructions: List[TAC]):
        """Generate all user-defined functions"""
        i = 0
        while i < len(instructions):
            instr = instructions[i]
            
            if instr.op == 'FUNC_BEGIN':
                func_name = instr.arg1
                self.current_function = func_name
                self.function_code = []
                self.label_map = {}
                self.last_label = None
                
                # Collect parameters
                params = []
                j = i + 1
                while j < len(instructions) and instructions[j].op == 'PARAM':
                    params.append(instructions[j].arg1)
                    j += 1
                
                # Start function with proper signature
                param_list = ", ".join([f"int {p}" for p in params])
                self.emit(f"int {func_name}({param_list}) {{")
                self.indent_level += 1
                
                # Declare local temp variables
                local_temps = set()
                k = i
                while k < len(instructions):
                    if instructions[k].op == 'FUNC_END':
                        break
                    if instructions[k].result and instructions[k].result.startswith('t'):
                        local_temps.add(instructions[k].result)
                    k += 1
                
                if local_temps:
                    self.emit("// Temporary variables")
                    for temp in sorted(local_temps):
                        self.emit(f"int {temp} = 0;")
                
                # Declare local variables (excluding parameters)
                local_vars = set()
                k = i
                while k < len(instructions):
                    if instructions[k].op == 'FUNC_END':
                        break
                    if instructions[k].op == 'ASSIGN':
                        var = instructions[k].result
                        if var and not var.startswith('t') and var not in self.global_vars and var not in params:
                            local_vars.add(var)
                    k += 1
                
                if local_vars:
                    self.emit("// Local variables")
                    for var in sorted(local_vars):
                        self.emit(f"int {var} = 0;")
                
                if local_temps or local_vars:
                    self.emit_blank()
                
                # Generate function body - start from first non-PARAM instruction
                j = i + 1
                while j < len(instructions) and instructions[j].op == 'PARAM':
                    j += 1
                
                # Now generate the body
                while j < len(instructions):
                    instr = instructions[j]
                    if instr.op == 'FUNC_END':
                        # Check if last instruction was a label
                        if self.last_label:
                            self.emit(";  // Empty statement after label")
                        i = j  # Update i to FUNC_END position
                        break
                    self._generate_instruction(instr)
                    j += 1
                
                # End function
                self.indent_level -= 1
                self.emit("}")
                self.emit_blank()
                
                # Save function code
                self.functions[func_name] = self.function_code[:]
                self.c_code.extend(self.function_code)
                self.current_function = None
                self.function_code = []
            
            i += 1
    
    def _generate_main_function(self, instructions: List[TAC]):
        """Generate main function with global scope code"""
        self.emit("int main() {")
        self.indent_level += 1
        self.last_label = None
        
        # Collect temps used in global scope
        global_temps = set()
        for instr in instructions:
            if instr.op not in ['FUNC_BEGIN', 'FUNC_END', 'PARAM']:
                # Check if this is outside a function
                in_function = False
                for check_instr in instructions[:instructions.index(instr)]:
                    if check_instr.op == 'FUNC_BEGIN':
                        in_function = True
                    elif check_instr.op == 'FUNC_END':
                        in_function = False
                
                if not in_function and instr.result and instr.result.startswith('t'):
                    global_temps.add(instr.result)
        
        if global_temps:
            self.emit("// Temporary variables")
            for temp in sorted(global_temps):
                self.emit(f"int {temp} = 0;")
            self.emit_blank()
        
        # Generate global scope instructions (outside functions)
        self.pending_params = []
        in_function = False
        for instr in instructions:
            if instr.op == 'FUNC_BEGIN':
                in_function = True
            elif instr.op == 'FUNC_END':
                in_function = False
            elif not in_function:
                self._generate_instruction(instr)
        
        # Check if last instruction was a label
        if self.last_label:
            self.emit(";  // Empty statement after label")
        
        self.emit_blank()
        self.emit("return 0;")
        self.indent_level -= 1
        self.emit("}")
    
    def _generate_instruction(self, instr: TAC):
        """Generate C code for a single TAC instruction"""
        op = instr.op
        
        # Skip function boundary markers in body generation
        if op in ['FUNC_BEGIN', 'FUNC_END']:
            return
        
        # Handle PARAM instructions - collect them for the next CALL
        if op == 'PARAM':
            self.pending_params.append(instr.arg1)
            return
        
        # Labels
        if op == 'LABEL':
            self.indent_level -= 1  # Unindent labels
            self.emit(f"{instr.arg1}:")
            self.last_label = instr.arg1
            self.indent_level += 1
            return
        
        # If we're generating a non-label instruction, reset last_label
        self.last_label = None
        
        # Jumps
        if op == 'GOTO':
            self.emit(f"goto {instr.arg1};")
            return
        
        if op == 'IF_FALSE':
            self.emit(f"if (!{instr.arg1}) goto {instr.result};")
            return
        
        if op == 'IF_TRUE':
            self.emit(f"if ({instr.arg1}) goto {instr.result};")
            return
        
        # Assignment
        if op == 'ASSIGN':
            self.emit(f"{instr.result} = {self._format_value(instr.arg1)};")
            return
        
        # Binary operations
        if op in ['+', '-', '*', '/', '%', '==', '!=', '<', '>', '<=', '>=', '&&', '||']:
            left = self._format_value(instr.arg1)
            right = self._format_value(instr.arg2)
            self.emit(f"{instr.result} = {left} {op} {right};")
            return
        
        # Unary operations
        if op == 'UNARY':
            operator = instr.arg1
            operand = self._format_value(instr.arg2)
            self.emit(f"{instr.result} = {operator}{operand};")
            return
        
        # Function calls
        if op == 'CALL':
            func_name = instr.arg1
            n_args = int(instr.arg2) if instr.arg2 else 0
            result = instr.result
            
            # Get the parameters for this call
            call_params = self.pending_params[-n_args:] if n_args > 0 else []
            self.pending_params = self.pending_params[:-n_args] if n_args > 0 else []
            
            # Special handling for built-in functions
            if func_name == 'print':
                # Generate proper printf with actual arguments
                if call_params:
                    # Build format string and args based on parameter types
                    format_parts = []
                    args = []
                    for p in call_params:
                        formatted = self._format_value(p)
                        # Check if it's a string literal
                        if isinstance(p, str) and p.startswith('"') and p.endswith('"'):
                            format_parts.append("%s")
                            args.append(formatted)
                        else:
                            format_parts.append("%d")
                            args.append(formatted)
                    
                    format_str = " ".join(format_parts)
                    args_str = ", ".join(args)
                    self.emit(f'printf("{format_str}\\n", {args_str});')
                else:
                    self.emit(f'printf("\\n");')
            elif func_name == 'input':
                self.emit(f'// input() call - not implemented')
                if result:
                    self.emit(f'{result} = 0;')
            else:
                # User-defined function with proper arguments
                args_str = ", ".join([self._format_value(p) for p in call_params])
                if result:
                    self.emit(f"{result} = {func_name}({args_str});")
                else:
                    self.emit(f"{func_name}({args_str});")
            return
        
        # Return
        if op == 'RETURN':
            if instr.arg1:
                self.emit(f"return {self._format_value(instr.arg1)};")
            else:
                self.emit("return 0;")
            return
        
        # SEQ blocks
        if op == 'SEQ_BEGIN':
            self.emit("// Sequential block")
            self.emit("{")
            self.indent_level += 1
            return
        
        if op == 'SEQ_END':
            self.indent_level -= 1
            self.emit("}")
            return
        
        # PAR blocks - generate pthread code
        if op == 'PAR_BEGIN':
            self.emit("// Parallel block (simplified - sequential execution)")
            self.emit("{")
            self.indent_level += 1
            self.in_par_block = True
            return
        
        if op == 'PAR_END':
            self.indent_level -= 1
            self.emit("}")
            self.in_par_block = False
            return
        
        if op == 'THREAD_START':
            self.emit(f"// Thread {instr.arg1 if instr.arg1 else 0} start")
            return
        
        if op == 'THREAD_END':
            self.emit(f"// Thread {instr.arg1 if instr.arg1 else 0} end")
            return
        
        # Channel operations
        if op == 'CHANNEL_CREATE':
            self.emit(f"// Channel {instr.arg2} created ({instr.arg1})")
            return
        
        if op == 'METHOD_CALL':
            self.emit(f"// Method call: {instr.arg1}.{instr.arg2}()")
            if instr.result:
                self.emit(f"{instr.result} = 0;  // Method result")
            return
        
        if op == 'METHOD_ARGS':
            return  # Skip - already handled in METHOD_CALL
        
        # Default: comment out unknown instructions
        self.emit(f"// TAC: {instr}")
    
    def _format_value(self, value) -> str:
        """Format a value for C code"""
        if value is None:
            return "0"
        
        # String literal
        if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
            return value.replace('\\n', '\\n')  # Preserve escape sequences
        
        # Boolean literals
        if value == "true":
            return "1"
        if value == "false":
            return "0"
        
        # Numbers and variables
        return str(value)
    
    def print_code(self):
        """Print the generated C code"""
        print("\n=== Generated C Code ===")
        print("\n".join(self.c_code))
    
    def save_to_file(self, filename: str):
        """Save generated C code to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("\n".join(self.c_code))
        print(f"\n✓ C code saved to: {filename}")
