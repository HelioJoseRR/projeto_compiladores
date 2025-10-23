"""
Minipar Compiler - Main Driver
Frontend compiler that performs lexical analysis, parsing, semantic analysis, code generation, and C code generation
"""

import sys
import io
import os
try:
    from src.lexer import Lexer
    from src.parser import Parser
    from src.semantic import SemanticAnalyzer
    from src.codegen import CodeGenerator
    from src.c_codegen import CCodeGenerator
    from src.backend import Backend
except ImportError:
    from lexer import Lexer
    from parser import Parser
    from semantic import SemanticAnalyzer
    from codegen import CodeGenerator
    from c_codegen import CCodeGenerator
    from backend import Backend

# Fix encoding for Windows console
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        # Python < 3.7
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def compile_source(source: str, show_tokens: bool = False, show_ast: bool = False, 
                   show_semantic: bool = False, generate_c: bool = False, c_output: str = None,
                   compile_asm: bool = False, compile_exe: bool = False, target_arch: str = "native"):
    """
    Compile Minipar source code to three-address code and optionally C code, assembly, or executable
    
    Args:
        source: Source code string
        show_tokens: If True, print tokens
        show_ast: If True, print AST
        show_semantic: If True, print semantic analysis details
        generate_c: If True, generate C code
        c_output: Output filename for C code (default: output.c)
        compile_asm: If True, compile to assembly
        compile_exe: If True, compile to executable
        target_arch: Target architecture (native, armv7, x86_64)
    
    Returns:
        Tuple of (CodeGenerator, CCodeGenerator if generated)
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
        
        # Semantic Analysis
        print("=== Semantic Analysis ===")
        semantic = SemanticAnalyzer()
        is_valid = semantic.analyze(ast)
        
        if show_semantic:
            semantic.symbol_table.print_table()
        
        if not is_valid:
            print("❌ Semantic errors found:")
            semantic.print_errors()
            sys.exit(1)
        
        print(f"✓ Semantic analysis complete: No errors found\n")
        
        # Code Generation (TAC)
        print("=== Code Generation (TAC) ===")
        codegen = CodeGenerator()
        codegen.generate(ast)
        
        print(f"✓ Code generation complete: {len(codegen.code)} instructions generated\n")
        
        codegen.print_code()
        
        # C Code Generation (if requested or needed for backend)
        c_gen = None
        
        # Determine C filename
        if c_output:
            c_filename = c_output if c_output.endswith('.c') else c_output + '.c'
        else:
            c_filename = "output.c"
        
        if generate_c or compile_asm or compile_exe:
            print("\n" + "=" * 60)
            print("=== C Code Generation ===")
            c_gen = CCodeGenerator()
            c_code = c_gen.generate(codegen.code)
            
            print(f"✓ C code generation complete\n")
            
            if generate_c:
                c_gen.print_code()
            
            # Save to file
            c_gen.save_to_file(c_filename)
        
        # Backend compilation (if requested)
        if compile_asm or compile_exe:
            print("\n" + "=" * 60)
            print("=== Backend Compilation ===")
            backend = Backend(target_arch=target_arch)
            
            # Get backend info
            info = backend.get_info()
            print(f"GCC: {info.get('gcc_version', 'Unknown')}")
            print(f"Architecture: {target_arch}\n")
            
            # Determine output filenames
            import os
            base_name = os.path.splitext(c_filename)[0]
            asm_file = f"{base_name}.s"
            exe_file = f"{base_name}.exe" if sys.platform == "win32" else base_name
            
            # Compile to assembly
            if compile_asm:
                print("Compiling to assembly...")
                success, msg = backend.compile_to_assembly(c_filename, asm_file)
                print(msg)
                if not success:
                    sys.exit(1)
            
            # Compile to executable
            if compile_exe:
                print("\nCompiling to executable...")
                success, msg = backend.compile_to_executable(c_filename, exe_file)
                print(msg)
                if not success:
                    sys.exit(1)
            
            print("=" * 60)
        
        return codegen, c_gen
        
    except SyntaxError as e:
        print(f"\n❌ Compilation Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def compile_file(filename: str, show_tokens: bool = False, show_ast: bool = False, 
                 show_semantic: bool = False, generate_c: bool = False, c_output: str = None,
                 compile_asm: bool = False, compile_exe: bool = False, target_arch: str = "native"):
    """Compile a Minipar source file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        print(f"Compiling: {filename}")
        print("=" * 60)
        return compile_source(source, show_tokens, show_ast, show_semantic, generate_c, c_output,
                            compile_asm, compile_exe, target_arch)
        
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python compiler.py [options] <source_file>")
        print("   or: python compiler.py <source_file> [options]")
        print()
        print("Options:")
        print("  --tokens: Show token stream")
        print("  --ast: Show abstract syntax tree")
        print("  --semantic: Show semantic analysis details")
        print("  --generate-c: Generate C code")
        print("  --output <file>: Specify C output file (default: output.c)")
        print("  --asm: Compile to assembly")
        print("  --exe: Compile to executable")
        print("  --arch <arch>: Target architecture (native, armv7, x86_64)")
        sys.exit(1)
    
    # Find the filename (first non-flag argument)
    filename = None
    for arg in sys.argv[1:]:
        if not arg.startswith('--') and arg != sys.argv[0]:
            # Skip if it's a value for a flag
            prev_idx = sys.argv.index(arg) - 1
            if prev_idx > 0 and sys.argv[prev_idx] in ['--output', '--arch']:
                continue
            filename = arg
            break
    
    if not filename:
        print("Error: No source file specified")
        sys.exit(1)
    
    show_tokens = '--tokens' in sys.argv
    show_ast = '--ast' in sys.argv
    show_semantic = '--semantic' in sys.argv
    generate_c = '--generate-c' in sys.argv
    compile_asm = '--asm' in sys.argv
    compile_exe = '--exe' in sys.argv
    
    c_output = None
    if '--output' in sys.argv:
        idx = sys.argv.index('--output')
        if idx + 1 < len(sys.argv):
            c_output = sys.argv[idx + 1]
    
    target_arch = "native"
    if '--arch' in sys.argv:
        idx = sys.argv.index('--arch')
        if idx + 1 < len(sys.argv):
            target_arch = sys.argv[idx + 1]
    
    compile_file(filename, show_tokens, show_ast, show_semantic, generate_c, c_output,
                compile_asm, compile_exe, target_arch)


if __name__ == '__main__':
    main()
