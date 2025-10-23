"""
Semantic Analyzer for Minipar Language
Performs type checking and semantic validation
"""

from typing import Optional, List
try:
    from src.ast_nodes import *
    from src.symbol_table import SymbolTable, SymbolType, Symbol
except ImportError:
    from ast_nodes import *
    from symbol_table import SymbolTable, SymbolType, Symbol


class SemanticError(Exception):
    """Exception raised for semantic errors"""
    pass


class SemanticAnalyzer:
    """Performs semantic analysis on the AST"""
    
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors: List[str] = []
        self.current_function_return_type: Optional[str] = None
        self.in_loop = False  # Track if we're inside a loop (for break/continue)
        
        # Built-in functions
        self._initialize_builtins()
    
    def _initialize_builtins(self):
        """Initialize built-in functions in global scope"""
        builtins = [
            ("print", "void", ["any"]),  # Variable args, simplified
            ("input", "string", ["string"]),
            ("len", "number", ["any"]),
            ("to_string", "string", ["any"]),
            ("to_number", "number", ["string"]),
            ("sleep", "void", ["number"]),
            # Math functions
            ("pow", "number", ["number", "number"]),
            ("sqrt", "number", ["number"]),
            ("abs", "number", ["number"]),
            # String functions
            ("isalpha", "bool", ["string"]),
            ("isnum", "bool", ["string"]),
        ]
        
        for name, return_type, param_types in builtins:
            self.symbol_table.add_symbol(
                name, SymbolType.FUNCTION, return_type,
                line=0, is_initialized=True,
                param_types=param_types, return_type=return_type
            )
    
    def add_error(self, message: str, line: int = 0):
        """Add a semantic error"""
        self.errors.append(f"Semantic error at line {line}: {message}")
    
    def analyze(self, node: ASTNode) -> bool:
        """
        Analyze the AST and return True if no errors
        """
        self.errors = []
        try:
            self.visit(node)
            return len(self.errors) == 0
        except SemanticError as e:
            self.errors.append(str(e))
            return False
    
    def visit(self, node: ASTNode) -> Optional[str]:
        """
        Visit a node and return its type
        Uses visitor pattern with dynamic dispatch
        """
        method_name = f'visit_{node.__class__.__name__}'
        method = getattr(self, method_name, self.generic_visit)
        return method(node)
    
    def generic_visit(self, node: ASTNode):
        """Fallback for nodes without specific visitor"""
        raise SemanticError(f"No visitor method for {node.__class__.__name__}")
    
    # ========== Program and Declarations ==========
    
    def visit_Program(self, node: Program) -> None:
        """Visit program node"""
        for declaration in node.declarations:
            self.visit(declaration)
    
    def visit_VarDecl(self, node: VarDecl) -> None:
        """Visit variable declaration"""
        # Check if variable already declared in current scope
        if self.symbol_table.lookup_local(node.name):
            self.add_error(f"Variable '{node.name}' already declared in current scope")
            return
        
        # Check initializer type if present
        if node.initializer:
            init_type = self.visit(node.initializer)
            if not self.is_type_compatible(node.type, init_type):
                self.add_error(
                    f"Type mismatch: cannot assign {init_type} to {node.type} "
                    f"for variable '{node.name}'"
                )
        
        # Add to symbol table
        self.symbol_table.add_symbol(
            node.name, SymbolType.VARIABLE, node.type,
            line=0, is_initialized=(node.initializer is not None)
        )
    
    def visit_FuncDecl(self, node: FuncDecl) -> None:
        """Visit function declaration"""
        # Check if function already declared in current scope
        if self.symbol_table.lookup_local(node.name):
            self.add_error(f"Function '{node.name}' already declared in current scope")
            return
        
        # Extract parameter types
        param_types = [param.type for param in node.parameters]
        
        # Add function to symbol table
        self.symbol_table.add_symbol(
            node.name, SymbolType.FUNCTION, node.return_type,
            line=0, is_initialized=True,
            param_types=param_types, return_type=node.return_type
        )
        
        # Enter function scope
        self.symbol_table.enter_scope(f"func_{node.name}")
        
        # Add parameters to function scope
        for param in node.parameters:
            if self.symbol_table.lookup_local(param.name):
                self.add_error(f"Parameter '{param.name}' already declared")
            else:
                self.symbol_table.add_symbol(
                    param.name, SymbolType.PARAMETER, param.type,
                    line=0, is_initialized=True
                )
        
        # Set current function return type for checking return statements
        old_return_type = self.current_function_return_type
        self.current_function_return_type = node.return_type
        
        # Visit function body
        self.visit(node.body)
        
        # Restore previous return type
        self.current_function_return_type = old_return_type
        
        # Exit function scope
        self.symbol_table.exit_scope()
    
    def visit_ChannelDecl(self, node: ChannelDecl) -> None:
        """Visit channel declaration"""
        # Check if channel already declared
        if self.symbol_table.lookup_local(node.name):
            self.add_error(f"Channel '{node.name}' already declared in current scope")
            return
        
        # Add channel to symbol table
        self.symbol_table.add_symbol(
            node.name, SymbolType.CHANNEL, node.channel_type,
            line=0, is_initialized=True,
            channel_type=node.channel_type
        )
        
        # Visit arguments
        for arg in node.arguments:
            self.visit(arg)
    
    # ========== Statements ==========
    
    def visit_Block(self, node: Block) -> None:
        """Visit block statement"""
        # Enter new scope for block
        self.symbol_table.enter_scope("block")
        
        for stmt in node.statements:
            self.visit(stmt)
        
        # Exit block scope
        self.symbol_table.exit_scope()
    
    def visit_SeqBlock(self, node: SeqBlock) -> None:
        """Visit SEQ block"""
        self.symbol_table.enter_scope("seq_block")
        
        for stmt in node.statements:
            self.visit(stmt)
        
        self.symbol_table.exit_scope()
    
    def visit_ParBlock(self, node: ParBlock) -> None:
        """Visit PAR block"""
        self.symbol_table.enter_scope("par_block")
        
        for stmt in node.statements:
            self.visit(stmt)
        
        self.symbol_table.exit_scope()
    
    def visit_IfStmt(self, node: IfStmt) -> None:
        """Visit if statement"""
        # Check condition type
        cond_type = self.visit(node.condition)
        if cond_type != "bool" and cond_type != "any":
            self.add_error(f"If condition must be boolean, got {cond_type}")
        
        # Visit branches
        self.visit(node.then_branch)
        if node.else_branch:
            self.visit(node.else_branch)
    
    def visit_WhileStmt(self, node: WhileStmt) -> None:
        """Visit while statement"""
        # Check condition type
        cond_type = self.visit(node.condition)
        if cond_type != "bool" and cond_type != "any":
            self.add_error(f"While condition must be boolean, got {cond_type}")
        
        # Track that we're in a loop
        old_in_loop = self.in_loop
        self.in_loop = True
        
        # Visit body
        self.visit(node.body)
        
        # Restore loop state
        self.in_loop = old_in_loop
    
    def visit_ReturnStmt(self, node: ReturnStmt) -> None:
        """Visit return statement"""
        if self.current_function_return_type is None:
            self.add_error("Return statement outside function")
            return
        
        if node.value:
            return_type = self.visit(node.value)
            if not self.is_type_compatible(self.current_function_return_type, return_type):
                self.add_error(
                    f"Return type mismatch: expected {self.current_function_return_type}, "
                    f"got {return_type}"
                )
        else:
            if self.current_function_return_type != "void":
                self.add_error(
                    f"Missing return value: function should return {self.current_function_return_type}"
                )
    
    def visit_BreakStmt(self, node: BreakStmt) -> None:
        """Visit break statement"""
        if not self.in_loop:
            self.add_error("Break statement outside loop")
    
    def visit_ContinueStmt(self, node: ContinueStmt) -> None:
        """Visit continue statement"""
        if not self.in_loop:
            self.add_error("Continue statement outside loop")
    
    def visit_ExprStmt(self, node: ExprStmt) -> None:
        """Visit expression statement"""
        self.visit(node.expression)
    
    # ========== Expressions ==========
    
    def visit_Assignment(self, node: Assignment) -> str:
        """Visit assignment"""
        # Check if variable exists
        symbol = self.symbol_table.lookup(node.name)
        if not symbol:
            self.add_error(f"Undefined variable '{node.name}'")
            return "any"
        
        # Check if it's assignable (not a function)
        if symbol.symbol_type == SymbolType.FUNCTION:
            self.add_error(f"Cannot assign to function '{node.name}'")
            return "any"
        
        # Check type compatibility
        value_type = self.visit(node.value)
        if not self.is_type_compatible(symbol.data_type, value_type):
            self.add_error(
                f"Type mismatch: cannot assign {value_type} to {symbol.data_type} "
                f"for variable '{node.name}'"
            )
        
        # Mark as initialized
        symbol.is_initialized = True
        
        return symbol.data_type
    
    def visit_BinaryOp(self, node: BinaryOp) -> str:
        """Visit binary operation"""
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)
        
        # Arithmetic operators
        if node.operator in ['+', '-', '*', '/', '%']:
            if left_type == "string" and node.operator == '+':
                # String concatenation
                return "string"
            if left_type != "number" or right_type != "number":
                if left_type != "any" and right_type != "any":
                    self.add_error(
                        f"Arithmetic operator '{node.operator}' requires numbers, "
                        f"got {left_type} and {right_type}"
                    )
            return "number"
        
        # Comparison operators
        elif node.operator in ['<', '>', '<=', '>=']:
            if left_type != "number" or right_type != "number":
                if left_type != "any" and right_type != "any":
                    self.add_error(
                        f"Comparison operator '{node.operator}' requires numbers, "
                        f"got {left_type} and {right_type}"
                    )
            return "bool"
        
        # Equality operators
        elif node.operator in ['==', '!=']:
            # Allow comparison of any types
            return "bool"
        
        # Logical operators
        elif node.operator in ['&&', '||']:
            if left_type != "bool" and left_type != "any":
                self.add_error(f"Logical operator requires boolean, got {left_type}")
            if right_type != "bool" and right_type != "any":
                self.add_error(f"Logical operator requires boolean, got {right_type}")
            return "bool"
        
        else:
            self.add_error(f"Unknown binary operator '{node.operator}'")
            return "any"
    
    def visit_UnaryOp(self, node: UnaryOp) -> str:
        """Visit unary operation"""
        operand_type = self.visit(node.operand)
        
        if node.operator == '-':
            if operand_type != "number" and operand_type != "any":
                self.add_error(f"Unary minus requires number, got {operand_type}")
            return "number"
        
        elif node.operator == '!':
            if operand_type != "bool" and operand_type != "any":
                self.add_error(f"Logical NOT requires boolean, got {operand_type}")
            return "bool"
        
        else:
            self.add_error(f"Unknown unary operator '{node.operator}'")
            return "any"
    
    def visit_FuncCall(self, node: FuncCall) -> str:
        """Visit function call"""
        # Look up function
        symbol = self.symbol_table.lookup(node.name)
        if not symbol:
            self.add_error(f"Undefined function '{node.name}'")
            return "any"
        
        if symbol.symbol_type != SymbolType.FUNCTION:
            self.add_error(f"'{node.name}' is not a function")
            return "any"
        
        # Check argument count (relaxed for built-ins like print)
        if symbol.param_types and node.name not in ['print']:
            if len(node.arguments) != len(symbol.param_types):
                self.add_error(
                    f"Function '{node.name}' expects {len(symbol.param_types)} arguments, "
                    f"got {len(node.arguments)}"
                )
        
        # Check argument types
        for i, arg in enumerate(node.arguments):
            arg_type = self.visit(arg)
            if symbol.param_types and i < len(symbol.param_types):
                expected_type = symbol.param_types[i]
                if expected_type != "any" and not self.is_type_compatible(expected_type, arg_type):
                    self.add_error(
                        f"Argument {i+1} to '{node.name}': expected {expected_type}, "
                        f"got {arg_type}"
                    )
        
        return symbol.return_type or "void"
    
    def visit_MethodCall(self, node: MethodCall) -> str:
        """Visit method call"""
        # Look up object
        symbol = self.symbol_table.lookup(node.object)
        if not symbol:
            self.add_error(f"Undefined object '{node.object}'")
            return "any"
        
        # For channels, allow send, receive, close methods
        if symbol.symbol_type == SymbolType.CHANNEL:
            if node.method in ['send', 'receive', 'close']:
                if node.method == 'send':
                    return "string"  # send returns response string from server
                elif node.method == 'receive':
                    return "string"  # receive returns string
                else:  # close
                    return "void"  # close returns void
            else:
                self.add_error(f"Unknown method '{node.method}' for channel '{node.object}'")
                return "any"
        
        # For other types, method calls not yet supported
        self.add_error(f"Method calls not supported for type {symbol.data_type}")
        return "any"
    
    def visit_Variable(self, node: Variable) -> str:
        """Visit variable reference"""
        symbol = self.symbol_table.lookup(node.name)
        if not symbol:
            self.add_error(f"Undefined variable '{node.name}'")
            return "any"
        
        # Check if variable is initialized (optional warning)
        if symbol.symbol_type == SymbolType.VARIABLE and not symbol.is_initialized:
            # This is a warning, not an error
            pass
        
        return symbol.data_type
    
    def visit_NumberLiteral(self, node: NumberLiteral) -> str:
        """Visit number literal"""
        return "number"
    
    def visit_StringLiteral(self, node: StringLiteral) -> str:
        """Visit string literal"""
        return "string"
    
    def visit_BoolLiteral(self, node: BoolLiteral) -> str:
        """Visit boolean literal"""
        return "bool"
    
    # ========== Helper Methods ==========
    
    def is_type_compatible(self, expected: str, actual: str) -> bool:
        """Check if types are compatible"""
        if expected == actual:
            return True
        if expected == "any" or actual == "any":
            return True
        # bool can be used as number (0 or 1)
        if expected == "number" and actual == "bool":
            return True
        return False
    
    def print_errors(self):
        """Print all semantic errors"""
        if self.errors:
            print("\n=== Semantic Errors ===")
            for error in self.errors:
                print(f"  {error}")
        else:
            print("\n✓ No semantic errors found")
    
    def get_errors(self) -> List[str]:
        """Get list of errors"""
        return self.errors.copy()
