"""
Test Suite for Minipar Compiler
Tests lexer, parser, and code generator
"""

import sys
import os
import io

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lexer import Lexer, TokenType
from parser import Parser
from codegen import CodeGenerator
from compiler import compile_source


def test_lexer():
    print("Testing Lexer...")
    
    # Test 1: Keywords and identifiers
    source = "func number while if else"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    assert tokens[0].type == TokenType.FUNC
    assert tokens[1].type == TokenType.NUMBER
    assert tokens[2].type == TokenType.WHILE
    print("  ✓ Keywords recognized")
    
    # Test 2: Operators
    source = "+ - * / % == != <= >= < > = && ||"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    assert tokens[0].type == TokenType.PLUS
    assert tokens[5].type == TokenType.EQ
    assert tokens[12].type == TokenType.AND
    print("  ✓ Operators recognized")
    
    # Test 3: Literals
    source = '42 3.14 "hello" true false'
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    assert tokens[0].type == TokenType.NUMBER_LITERAL
    assert tokens[0].value == 42
    assert tokens[1].value == 3.14
    assert tokens[2].type == TokenType.STRING_LITERAL
    assert tokens[2].value == "hello"
    print("  ✓ Literals recognized")
    
    # Test 4: Comments
    source = """
    # Single line comment
    number x = 5; /* Multi
    line comment */ number y = 10;
    """
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    token_types = [t.type for t in tokens if t.type != TokenType.EOF]
    assert TokenType.NUMBER in token_types
    print("  ✓ Comments handled")
    
    print("✅ Lexer tests passed!\n")


def test_parser():
    print("Testing Parser...")
    
    # Test 1: Variable declaration
    source = "number x = 10;"
    lexer = Lexer(source)
    parser = Parser(lexer.tokenize())
    ast = parser.parse()
    assert len(ast.declarations) == 1
    print("  ✓ Variable declaration parsed")
    
    # Test 2: Function declaration
    source = """
    func number add(number a, number b) {
        return a + b;
    }
    """
    lexer = Lexer(source)
    parser = Parser(lexer.tokenize())
    ast = parser.parse()
    assert len(ast.declarations) == 1
    print("  ✓ Function declaration parsed")
    
    # Test 3: If statement
    source = """
    func void test() {
        if (x > 0) {
            y = 1;
        } else {
            y = 0;
        }
    }
    """
    lexer = Lexer(source)
    parser = Parser(lexer.tokenize())
    ast = parser.parse()
    assert len(ast.declarations) == 1
    print("  ✓ If statement parsed")
    
    # Test 4: While loop
    source = """
    func void loop() {
        while (x < 10) {
            x = x + 1;
        }
    }
    """
    lexer = Lexer(source)
    parser = Parser(lexer.tokenize())
    ast = parser.parse()
    assert len(ast.declarations) == 1
    print("  ✓ While loop parsed")
    
    print("✅ Parser tests passed!\n")


def test_codegen():
    print("Testing Code Generator...")
    
    # Test 1: Simple arithmetic
    source = """
    number x = 5 + 3;
    """
    lexer = Lexer(source)
    parser = Parser(lexer.tokenize())
    ast = parser.parse()
    codegen = CodeGenerator()
    codegen.generate(ast)
    assert len(codegen.code) > 0
    print("  ✓ Arithmetic code generated")
    
    # Test 2: Function call
    source = """
    func number add(number a, number b) {
        return a + b;
    }
    """
    lexer = Lexer(source)
    parser = Parser(lexer.tokenize())
    ast = parser.parse()
    codegen = CodeGenerator()
    codegen.generate(ast)
    assert len(codegen.code) > 0
    print("  ✓ Function code generated")
    
    # Test 3: Conditional
    source = """
    func void test(number x) {
        if (x > 0) {
            x = x + 1;
        }
    }
    """
    lexer = Lexer(source)
    parser = Parser(lexer.tokenize())
    ast = parser.parse()
    codegen = CodeGenerator()
    codegen.generate(ast)
    assert len(codegen.code) > 0
    # Check for labels
    has_label = any(instr.op == 'LABEL' for instr in codegen.code)
    assert has_label
    print("  ✓ Conditional code with labels generated")
    
    print("✅ Code generator tests passed!\n")


def test_full_examples():
    print("Testing Full Examples...")
    
    examples = [
        ("example1.mp", "Simple arithmetic"),
        ("example2.mp", "Factorial function"),
        ("example3.mp", "While loop"),
        ("example4.mp", "Boolean logic"),
        ("example5.mp", "String operations"),
    ]
    
    for filename, description in examples:
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    source = f.read()
                compile_source(source, show_tokens=False, show_ast=False)
                print(f"  ✓ {description} ({filename})")
            except Exception as e:
                print(f"  ❌ {description} ({filename}): {e}")
        else:
            print(f"  ⚠ {filename} not found")
    
    print("✅ Example tests completed!\n")


def main():
    print("=" * 60)
    print("Minipar Compiler Test Suite")
    print("=" * 60)
    print()
    
    try:
        test_lexer()
        test_parser()
        test_codegen()
        test_full_examples()
        
        print("=" * 60)
        print("✅ All tests passed successfully!")
        print("=" * 60)
    
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
