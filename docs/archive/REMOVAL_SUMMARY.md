# Removal of --arch and --asm Flags - Summary

## Date
2025-10-24

## Reason
The `--arch` and `--asm` flags were incorrectly implemented and have been removed from the project.

## Changes Made

### 1. Source Code Changes

#### `src/compiler.py`
- Removed `target_arch` parameter from `compile_source()` function
- Removed `compile_asm` parameter from `compile_source()` function
- Removed `--arch` flag from command-line argument parsing
- Removed `--asm` flag from command-line argument parsing
- Updated help message to remove references to removed flags
- Simplified backend compilation to only support executable generation

#### `src/backend.py`
- Removed `target_arch` parameter from `Backend.__init__()`
- Removed `_find_gcc()` architecture detection logic
- Removed `compile_to_assembly()` method completely
- Removed architecture-specific compilation flags
- Removed `target_arch` from `get_info()` method
- Simplified `compile_to_executable()` to remove architecture handling
- Updated `compile_minipar_pipeline()` to remove assembly and architecture support
- Simplified command-line interface in `main()` function

### 2. Documentation Changes

#### `README.md`
- No changes needed (already didn't reference these flags)

#### `QUICK_REFERENCE.md`
- No changes needed (already didn't reference these flags)

#### `docs/tutorials/ARM_COMPILATION_GUIDE.md`
- Added deprecation notice at the top
- Marked entire guide as deprecated
- Added references to current documentation

#### `docs/tutorials/RUNNING_ASSEMBLY_GUIDE.md`
- Added deprecation notice at the top
- Marked entire guide as deprecated
- Updated "Quick Answer" section to reflect current state
- Added references to current documentation

#### `docs/tutorials/TUTORIAL.md`
- Removed `--asm` flag from compilation examples
- Removed `--arch` flag from compilation examples
- Updated "Complete Flag List" section
- Removed "Generate assembly only" example
- Removed "Both assembly and executable" example
- Updated command examples to use `compile.py` instead of `src\compiler.py`

#### Archive Documentation
- Left as-is for historical reference
- `docs/archive/PHASE5_COMPLETE.md` and others contain references but are historical

## Current Compilation Options

The compiler now supports the following options:

```bash
py compile.py <source_file> [options]

Options:
  --tokens              Show token stream
  --ast                 Show abstract syntax tree
  --semantic            Show semantic analysis details
  --generate-c          Generate C code
  --output <file>       Specify C output file (default: output.c)
  --exe                 Compile to executable
```

## Compilation Modes

1. **TAC Generation** (default):
   ```bash
   py compile.py examples\ex1.minipar
   ```

2. **C Code Generation**:
   ```bash
   py compile.py examples\ex1.minipar --generate-c
   ```

3. **Executable Generation**:
   ```bash
   py compile.py examples\ex1.minipar --exe
   ```

## Testing Results

All tests pass successfully after removal:

✅ Lexer tests
✅ Parser tests  
✅ Code generator tests
✅ Example compilation tests
✅ Executable generation and execution
✅ Runtime executor (src/runner.py)

## Verified Functionality

- ✅ Basic compilation to TAC
- ✅ Token and AST display
- ✅ C code generation
- ✅ Executable compilation with GCC
- ✅ Generated executables run correctly
- ✅ Runtime executor works (channels, sockets, etc.)
- ✅ All test suite passes

## Files Modified

### Source Code
- `src/compiler.py`
- `src/backend.py`

### Documentation
- `docs/tutorials/ARM_COMPILATION_GUIDE.md`
- `docs/tutorials/RUNNING_ASSEMBLY_GUIDE.md`
- `docs/tutorials/TUTORIAL.md`

### New Files
- `REMOVAL_SUMMARY.md` (this file)

## Breaking Changes

The following commands no longer work:

```bash
# These will be ignored or cause errors:
py compile.py file.minipar --asm
py compile.py file.minipar --arch armv7
py compile.py file.minipar --asm --arch x86_64
```

Users should instead use:

```bash
# For executable generation:
py compile.py file.minipar --exe
```

## Migration Guide

If you were using:
- `--asm` → Use `--exe` instead (generates executable directly)
- `--arch <arch>` → Remove (native compilation only)
- `--asm --exe` → Use `--exe` only

## Notes

- The runtime executor (src/runner.py) is unaffected by these changes
- All channel functionality remains intact
- GCC integration still works for native executable generation
- The project structure and all other features remain unchanged
