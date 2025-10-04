"""
Abstract Syntax Tree Node Definitions for Minipar Language
"""

from dataclasses import dataclass
from typing import List, Optional, Any


@dataclass
class ASTNode:
    """Base class for all AST nodes"""
    pass


@dataclass
class Program(ASTNode):
    declarations: List[ASTNode]


@dataclass
class VarDecl(ASTNode):
    type: str
    name: str
    initializer: Optional[ASTNode] = None


@dataclass
class FuncDecl(ASTNode):
    return_type: str
    name: str
    parameters: List[VarDecl]
    body: 'Block'


@dataclass
class Block(ASTNode):
    statements: List[ASTNode]


@dataclass
class IfStmt(ASTNode):
    condition: ASTNode
    then_branch: ASTNode
    else_branch: Optional[ASTNode] = None


@dataclass
class WhileStmt(ASTNode):
    condition: ASTNode
    body: ASTNode


@dataclass
class ReturnStmt(ASTNode):
    value: Optional[ASTNode] = None


@dataclass
class BreakStmt(ASTNode):
    pass


@dataclass
class ContinueStmt(ASTNode):
    pass


@dataclass
class ExprStmt(ASTNode):
    expression: ASTNode


@dataclass
class Assignment(ASTNode):
    name: str
    value: ASTNode


@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode


@dataclass
class UnaryOp(ASTNode):
    operator: str
    operand: ASTNode


@dataclass
class FuncCall(ASTNode):
    name: str
    arguments: List[ASTNode]


@dataclass
class Variable(ASTNode):
    name: str


@dataclass
class NumberLiteral(ASTNode):
    value: float


@dataclass
class StringLiteral(ASTNode):
    value: str


@dataclass
class BoolLiteral(ASTNode):
    value: bool
