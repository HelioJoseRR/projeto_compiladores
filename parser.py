"""
Parser for Minipar Language
Performs syntax analysis and builds an Abstract Syntax Tree (AST)
"""

from typing import List, Optional
from lexer import Token, TokenType, Lexer
from ast_nodes import *


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def error(self, msg: str):
        token = self.current()
        raise SyntaxError(f"Parser error at {token.line}:{token.column}: {msg}")
    
    def current(self) -> Token:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else self.tokens[-1]
    
    def peek(self, offset: int = 0) -> Token:
        pos = self.pos + offset
        return self.tokens[pos] if pos < len(self.tokens) else self.tokens[-1]
    
    def advance(self) -> Token:
        token = self.current()
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return token
    
    def match(self, *types: TokenType) -> bool:
        return self.current().type in types
    
    def consume(self, token_type: TokenType, msg: str = None) -> Token:
        if not self.match(token_type):
            msg = msg or f"Expected {token_type.name}"
            self.error(msg)
        return self.advance()
    
    def parse(self) -> Program:
        declarations = []
        while not self.match(TokenType.EOF):
            declarations.append(self.declaration())
        return Program(declarations)
    
    def declaration(self) -> ASTNode:
        if self.match(TokenType.FUNC):
            return self.func_declaration()
        return self.var_declaration()
    
    def func_declaration(self) -> FuncDecl:
        self.consume(TokenType.FUNC)
        return_type = self.type_specifier()
        name = self.consume(TokenType.IDENTIFIER, "Expected function name").value
        
        self.consume(TokenType.LPAREN)
        parameters = []
        
        if not self.match(TokenType.RPAREN):
            parameters.append(self.parameter())
            while self.match(TokenType.COMMA):
                self.advance()
                parameters.append(self.parameter())
        
        self.consume(TokenType.RPAREN)
        body = self.block()
        
        return FuncDecl(return_type, name, parameters, body)
    
    def parameter(self) -> VarDecl:
        param_type = self.type_specifier()
        name = self.consume(TokenType.IDENTIFIER, "Expected parameter name").value
        return VarDecl(param_type, name)
    
    def var_declaration(self) -> VarDecl:
        var_type = self.type_specifier()
        name = self.consume(TokenType.IDENTIFIER, "Expected variable name").value
        
        initializer = None
        if self.match(TokenType.ASSIGN):
            self.advance()
            initializer = self.expression()
        
        self.consume(TokenType.SEMICOLON, "Expected ';' after variable declaration")
        return VarDecl(var_type, name, initializer)
    
    def type_specifier(self) -> str:
        if self.match(TokenType.NUMBER):
            self.advance()
            return 'number'
        elif self.match(TokenType.STRING):
            self.advance()
            return 'string'
        elif self.match(TokenType.BOOL):
            self.advance()
            return 'bool'
        elif self.match(TokenType.VOID):
            self.advance()
            return 'void'
        elif self.match(TokenType.C_CHANNEL):
            self.advance()
            return 'c_channel'
        elif self.match(TokenType.S_CHANNEL):
            self.advance()
            return 's_channel'
        else:
            self.error("Expected type specifier")
    
    def block(self) -> Block:
        self.consume(TokenType.LBRACE)
        statements = []
        
        while not self.match(TokenType.RBRACE) and not self.match(TokenType.EOF):
            statements.append(self.statement())
        
        self.consume(TokenType.RBRACE)
        return Block(statements)
    
    def statement(self) -> ASTNode:
        if self.match(TokenType.IF):
            return self.if_statement()
        elif self.match(TokenType.WHILE):
            return self.while_statement()
        elif self.match(TokenType.RETURN):
            return self.return_statement()
        elif self.match(TokenType.BREAK):
            return self.break_statement()
        elif self.match(TokenType.CONTINUE):
            return self.continue_statement()
        elif self.match(TokenType.LBRACE):
            return self.block()
        elif self.match(TokenType.NUMBER, TokenType.STRING, TokenType.BOOL, 
                       TokenType.VOID, TokenType.C_CHANNEL, TokenType.S_CHANNEL):
            return self.var_declaration()
        else:
            return self.expression_statement()
    
    def if_statement(self) -> IfStmt:
        self.consume(TokenType.IF)
        self.consume(TokenType.LPAREN)
        condition = self.expression()
        self.consume(TokenType.RPAREN)
        
        then_branch = self.statement()
        else_branch = None
        
        if self.match(TokenType.ELSE):
            self.advance()
            else_branch = self.statement()
        
        return IfStmt(condition, then_branch, else_branch)
    
    def while_statement(self) -> WhileStmt:
        self.consume(TokenType.WHILE)
        self.consume(TokenType.LPAREN)
        condition = self.expression()
        self.consume(TokenType.RPAREN)
        body = self.statement()
        
        return WhileStmt(condition, body)
    
    def return_statement(self) -> ReturnStmt:
        self.consume(TokenType.RETURN)
        value = None
        
        if not self.match(TokenType.SEMICOLON):
            value = self.expression()
        
        self.consume(TokenType.SEMICOLON)
        return ReturnStmt(value)
    
    def break_statement(self) -> BreakStmt:
        self.consume(TokenType.BREAK)
        self.consume(TokenType.SEMICOLON)
        return BreakStmt()
    
    def continue_statement(self) -> ContinueStmt:
        self.consume(TokenType.CONTINUE)
        self.consume(TokenType.SEMICOLON)
        return ContinueStmt()
    
    def expression_statement(self) -> ExprStmt:
        expr = self.expression()
        self.consume(TokenType.SEMICOLON)
        return ExprStmt(expr)
    
    def expression(self) -> ASTNode:
        return self.assignment()
    
    def assignment(self) -> ASTNode:
        expr = self.logical_or()
        
        if self.match(TokenType.ASSIGN):
            self.advance()
            value = self.assignment()
            
            if isinstance(expr, Variable):
                return Assignment(expr.name, value)
            else:
                self.error("Invalid assignment target")
        
        return expr
    
    def logical_or(self) -> ASTNode:
        expr = self.logical_and()
        
        while self.match(TokenType.OR):
            op = self.advance().value
            right = self.logical_and()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def logical_and(self) -> ASTNode:
        expr = self.equality()
        
        while self.match(TokenType.AND):
            op = self.advance().value
            right = self.equality()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def equality(self) -> ASTNode:
        expr = self.comparison()
        
        while self.match(TokenType.EQ, TokenType.NEQ):
            op = self.advance().value
            right = self.comparison()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def comparison(self) -> ASTNode:
        expr = self.term()
        
        while self.match(TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            op = self.advance().value
            right = self.term()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def term(self) -> ASTNode:
        expr = self.factor()
        
        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = self.advance().value
            right = self.factor()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def factor(self) -> ASTNode:
        expr = self.unary()
        
        while self.match(TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
            op = self.advance().value
            right = self.unary()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def unary(self) -> ASTNode:
        if self.match(TokenType.NOT, TokenType.MINUS):
            op = self.advance().value
            expr = self.unary()
            return UnaryOp(op, expr)
        
        return self.call()
    
    def call(self) -> ASTNode:
        expr = self.primary()
        
        if self.match(TokenType.LPAREN):
            self.advance()
            arguments = []
            
            if not self.match(TokenType.RPAREN):
                arguments.append(self.expression())
                while self.match(TokenType.COMMA):
                    self.advance()
                    arguments.append(self.expression())
            
            self.consume(TokenType.RPAREN)
            
            if isinstance(expr, Variable):
                return FuncCall(expr.name, arguments)
            else:
                self.error("Invalid function call")
        
        return expr
    
    def primary(self) -> ASTNode:
        if self.match(TokenType.TRUE):
            self.advance()
            return BoolLiteral(True)
        
        if self.match(TokenType.FALSE):
            self.advance()
            return BoolLiteral(False)
        
        if self.match(TokenType.NUMBER_LITERAL):
            value = self.advance().value
            return NumberLiteral(value)
        
        if self.match(TokenType.STRING_LITERAL):
            value = self.advance().value
            return StringLiteral(value)
        
        if self.match(TokenType.IDENTIFIER):
            name = self.advance().value
            return Variable(name)
        
        if self.match(TokenType.LPAREN):
            self.advance()
            expr = self.expression()
            self.consume(TokenType.RPAREN)
            return expr
        
        self.error(f"Unexpected token: {self.current().type.name}")
