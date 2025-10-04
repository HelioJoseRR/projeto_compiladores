"""
Minipar Compiler - Main Driver
Frontend compiler that performs lexical analysis, parsing, and intermediate code generation
"""

import sys
import io
from lexer import Lexer
from parser import Parser
from codegen import CodeGenerator

# Fix encoding for Windows console
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        # Python < 3.7
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def compile_source(source: str, show_tokens: bool = False, show_ast: bool = False):
    """
    Compile Minipar source code to three-address code
    
    Args:
        source: Source code string
        show_tokens: If True, print tokens
        show_ast: If True, print AST
    
    Returns:
        CodeGenerator instance with generated code
    """
    try:
        # Lexical Analysis
        print("=== Lexical Analysis ===")
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        if show_tokens:
            print("\nTokens:")
            for token in tokens:
                if token.type.name != 'EOF':
                    print(f"  {token}")
        
        print(f"✓ Tokenization complete: {len(tokens)} tokens generated\n")
        
        # Syntax Analysis
        print("=== Syntax Analysis ===")
        parser = Parser(tokens)
        ast = parser.parse()
        
        if show_ast:
            print("\nAST:")
            print(f"  {ast}")
        
        print(f"✓ Parsing complete: AST with {len(ast.declarations)} declarations\n")
        
        # Code Generation
        print("=== Code Generation ===")
        codegen = CodeGenerator()
        codegen.generate(ast)
        
        print(f"✓ Code generation complete: {len(codegen.code)} instructions generated\n")
        
        codegen.print_code()
        
        return codegen
        
    except SyntaxError as e:
        print(f"\n❌ Compilation Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def compile_file(filename: str, show_tokens: bool = False, show_ast: bool = False):
    """Compile a Minipar source file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        print(f"Compiling: {filename}")
        print("=" * 60)
        return compile_source(source, show_tokens, show_ast)
        
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python compiler.py <source_file> [--tokens] [--ast]")
        print("  --tokens: Show token stream")
        print("  --ast: Show abstract syntax tree")
        sys.exit(1)
    
    filename = sys.argv[1]
    show_tokens = '--tokens' in sys.argv
    show_ast = '--ast' in sys.argv
    
    compile_file(filename, show_tokens, show_ast)


if __name__ == '__main__':
    main()
