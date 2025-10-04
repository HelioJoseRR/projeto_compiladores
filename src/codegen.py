"""
Intermediate Code Generator for Minipar Language
Generates three-address code from AST
"""

from typing import List, Dict, Optional
from ast_nodes import *


class TAC:
    """Three-Address Code instruction"""
    def __init__(self, op: str, arg1=None, arg2=None, result=None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result
    
    def __repr__(self):
        if self.op == 'CALL':
            # CALL nome_funcao n_args resultado
            return f"{self.op} {self.arg1} {self.arg2} {self.result}"
        elif self.op in ['LABEL', 'GOTO', 'PARAM', 'RETURN', 'FUNC_BEGIN', 'FUNC_END']:
            if self.arg1:
                return f"{self.op} {self.arg1}"
            return self.op
        elif self.op in ['IF_FALSE', 'IF_TRUE']:
            return f"{self.op} {self.arg1} GOTO {self.result}"
        elif self.op == 'ASSIGN':
            return f"{self.result} = {self.arg1}"
        elif self.op == 'UNARY':
            return f"{self.result} = {self.arg1} {self.arg2}"
        elif self.arg2 is None:
            return f"{self.result} = {self.arg1}"
        else:
            return f"{self.result} = {self.arg1} {self.op} {self.arg2}"


class CodeGenerator:
    def __init__(self):
        self.code: List[TAC] = []
        self.temp_count = 0
        self.label_count = 0
        self.symbol_table: Dict[str, str] = {}
    
    def new_temp(self) -> str:
        """Generate a new temporary variable"""
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp
    
    def new_label(self) -> str:
        """Generate a new label"""
        label = f"L{self.label_count}"
        self.label_count += 1
        return label
    
    def emit(self, op: str, arg1=None, arg2=None, result=None):
        """Emit a three-address code instruction"""
        self.code.append(TAC(op, arg1, arg2, result))
    
    def generate(self, node: ASTNode) -> Optional[str]:
        """Generate code for an AST node and return the result variable"""
        method_name = f'gen_{node.__class__.__name__}'
        method = getattr(self, method_name, self.generic_generate)
        return method(node)
    
    def generic_generate(self, node: ASTNode):
        raise NotImplementedError(f"Code generation not implemented for {node.__class__.__name__}")
    
    def gen_Program(self, node: Program) -> None:
        for decl in node.declarations:
            self.generate(decl)
    
    def gen_VarDecl(self, node: VarDecl) -> None:
        self.symbol_table[node.name] = node.type
        
        if node.initializer:
            value = self.generate(node.initializer)
            self.emit('ASSIGN', value, None, node.name)
    
    def gen_FuncDecl(self, node: FuncDecl) -> None:
        self.emit('FUNC_BEGIN', node.name)
        
        for param in node.parameters:
            self.symbol_table[param.name] = param.type
            self.emit('PARAM', param.name)
        
        self.generate(node.body)
        self.emit('FUNC_END', node.name)
    
    def gen_Block(self, node: Block) -> None:
        for stmt in node.statements:
            self.generate(stmt)
    
    def gen_IfStmt(self, node: IfStmt) -> None:
        condition = self.generate(node.condition)
        
        else_label = self.new_label()
        end_label = self.new_label()
        
        if node.else_branch:
            self.emit('IF_FALSE', condition, None, else_label)
            self.generate(node.then_branch)
            self.emit('GOTO', end_label)
            self.emit('LABEL', else_label)
            self.generate(node.else_branch)
            self.emit('LABEL', end_label)
        else:
            self.emit('IF_FALSE', condition, None, else_label)
            self.generate(node.then_branch)
            self.emit('LABEL', else_label)
    
    def gen_WhileStmt(self, node: WhileStmt) -> None:
        start_label = self.new_label()
        end_label = self.new_label()
        
        self.emit('LABEL', start_label)
        condition = self.generate(node.condition)
        self.emit('IF_FALSE', condition, None, end_label)
        self.generate(node.body)
        self.emit('GOTO', start_label)
        self.emit('LABEL', end_label)
    
    def gen_ReturnStmt(self, node: ReturnStmt) -> None:
        if node.value:
            result = self.generate(node.value)
            self.emit('RETURN', result)
        else:
            self.emit('RETURN')
    
    def gen_BreakStmt(self, node: BreakStmt) -> None:
        self.emit('BREAK')
    
    def gen_ContinueStmt(self, node: ContinueStmt) -> None:
        self.emit('CONTINUE')
    
    def gen_ExprStmt(self, node: ExprStmt) -> None:
        self.generate(node.expression)
    
    def gen_Assignment(self, node: Assignment) -> str:
        value = self.generate(node.value)
        self.emit('ASSIGN', value, None, node.name)
        return node.name
    
    def gen_BinaryOp(self, node: BinaryOp) -> str:
        left = self.generate(node.left)
        right = self.generate(node.right)
        result = self.new_temp()
        self.emit(node.operator, left, right, result)
        return result
    
    def gen_UnaryOp(self, node: UnaryOp) -> str:
        operand = self.generate(node.operand)
        result = self.new_temp()
        self.emit('UNARY', node.operator, operand, result)
        return result
    
    def gen_FuncCall(self, node: FuncCall) -> str:
        for arg in node.arguments:
            arg_result = self.generate(arg)
            self.emit('PARAM', arg_result)
        
        result = self.new_temp()
        self.emit('CALL', node.name, len(node.arguments), result)
        return result
    
    def gen_Variable(self, node: Variable) -> str:
        return node.name
    
    def gen_NumberLiteral(self, node: NumberLiteral) -> str:
        return str(node.value)
    
    def gen_StringLiteral(self, node: StringLiteral) -> str:
        return f'"{node.value}"'
    
    def gen_BoolLiteral(self, node: BoolLiteral) -> str:
        return str(node.value).lower()
    
    def print_code(self):
        """Print the generated three-address code"""
        print("\n=== Three-Address Code ===")
        for i, instruction in enumerate(self.code):
            print(f"{i:3d}: {instruction}")
    
    def get_code(self) -> List[TAC]:
        """Return the generated code"""
        return self.code
