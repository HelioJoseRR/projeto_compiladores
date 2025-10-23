# 🚀 MiniPar 2025.1 - Implementation Plan

**Goal:** Complete compiler pipeline from MiniPar → ARMv7 Assembly via C code and GCC

**Strategy:** Incremental development with testing at each phase

---

## 📋 Phase 1: Bug Fixes & Foundation (IMMEDIATE)

### Task 1.1: Fix Break/Continue Code Generation ⚠️
**Current Issue:** Generates `None = None` instead of proper control flow
**Solution:** Track loop labels and generate proper GOTO instructions

**Files to Modify:**
- `src/codegen.py` - Fix gen_BreakStmt and gen_ContinueStmt
- Add loop label stack management

**Estimated Time:** 1-2 hours

---

### Task 1.2: Add SEQ Keyword Support ⚠️
**Requirement:** Support SEQ { } blocks for explicit sequential execution

**Files to Modify:**
- `src/lexer.py` - Add SEQ token
- `src/parser.py` - Add SEQ block parsing
- `src/ast_nodes.py` - Add SeqBlock node
- `src/codegen.py` - Generate code for SEQ blocks

**Estimated Time:** 2-3 hours

---

### Task 1.3: Enhance PAR Support ⚠️
**Current Status:** PAR keyword exists but not fully implemented

**Files to Modify:**
- `src/parser.py` - Add PAR block parsing
- `src/ast_nodes.py` - Add ParBlock node
- `src/codegen.py` - Generate thread markers for PAR blocks

**Estimated Time:** 2-3 hours

---

### Task 1.4: Add Object Method Call Support ⚠️
**Requirement:** Support `obj.method()` syntax for channels

**Files to Modify:**
- `src/lexer.py` - DOT token already exists
- `src/parser.py` - Parse method calls
- `src/ast_nodes.py` - Add MethodCall node
- `src/codegen.py` - Generate method call code

**Estimated Time:** 3-4 hours

---

## 📋 Phase 2: Semantic Analysis (CRITICAL)

### Task 2.1: Enhanced Symbol Table
**Goal:** Complete symbol table with scope management

**New File:** `src/symbol_table.py`

**Features:**
- Scope hierarchy (global, function, block)
- Scope stack management
- Symbol properties (name, type, scope_level, is_initialized, line_declared)
- Lookup with scope resolution
- Duplicate declaration detection

**Estimated Time:** 4-6 hours

---

### Task 2.2: Semantic Analyzer
**Goal:** Type checking and semantic validation

**New File:** `src/semantic.py`

**Features:**
- Type checking for all operations
- Undefined variable detection
- Type compatibility validation
- Function signature matching
- Return type checking
- Break/continue context validation

**Integration:** Insert between parser and codegen in compiler.py

**Estimated Time:** 8-12 hours

---

## 📋 Phase 3: Bytecode Generator (OPTIONAL - Can skip for MVP)

### Task 3.1: Design Bytecode Format
**Decision:** Stack-based bytecode (simpler than register-based)

**Instruction Set Design:**
```
LOAD_CONST n    # Push constant onto stack
LOAD_VAR name   # Push variable value
STORE_VAR name  # Pop and store to variable
ADD, SUB, MUL, DIV, MOD  # Binary operations
NOT, NEG        # Unary operations
CALL name n     # Call function with n args
RETURN          # Return from function
JUMP label      # Unconditional jump
JUMP_IF_FALSE label  # Conditional jump
LABEL name      # Label marker
```

**New File:** `src/bytecode.py`

**Estimated Time:** 6-8 hours

---

### Task 3.2: TAC to Bytecode Converter
**Goal:** Convert three-address code to bytecode

**New File:** `src/bytecode_gen.py`

**Features:**
- Map TAC instructions to bytecode
- Stack management
- Label resolution
- Optimization opportunities

**Estimated Time:** 8-12 hours

---

## 📋 Phase 4: C Code Generator (CRITICAL - MVP)

### Task 4.1: C Code Generator from TAC
**Goal:** Direct TAC → C translation (skip bytecode)

**New File:** `src/c_codegen.py`

**Features:**
- Generate C headers and includes
- Convert variables to C declarations
- Convert functions to C functions
- Convert control flow to C syntax
- Handle temporaries as local variables
- Generate main() wrapper

**Example Output:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int soma(int num1, int num2) {
    int t0 = num1 + num2;
    int s = t0;
    int t5 = s + 10;
    return t5;
}

int main() {
    int a = 10;
    int b = 1;  // true
    int t6 = soma(2, 3);
    printf("%d\n", t6);
    return 0;
}
```

**Estimated Time:** 12-20 hours

---

### Task 4.2: Thread Support for PAR Blocks
**Goal:** Generate pthread code for parallel execution

**Features:**
- Create thread for each statement in PAR block
- Thread creation and joining
- Independent execution (no shared state)

**Example:**
```c
void* thread_func_0(void* arg) {
    stmt1;
    return NULL;
}

void* thread_func_1(void* arg) {
    stmt2;
    return NULL;
}

// In main:
pthread_t thread0, thread1;
pthread_create(&thread0, NULL, thread_func_0, NULL);
pthread_create(&thread1, NULL, thread_func_1, NULL);
pthread_join(thread0, NULL);
pthread_join(thread1, NULL);
```

**Estimated Time:** 6-10 hours

---

### Task 4.3: Socket Support for Channels
**Goal:** Generate socket code for c_channel and s_channel

**Features:**
- Client socket creation (c_channel)
- Server socket creation (s_channel)
- Send/receive operations
- Connection management

**Example:**
```c
// For c_channel
int sock = socket(AF_INET, SOCK_STREAM, 0);
struct sockaddr_in serv_addr;
// ... connect code ...

// For send
send(sock, data, len, 0);

// For receive
recv(sock, buffer, len, 0);
```

**Estimated Time:** 8-12 hours

---

## 📋 Phase 5: GCC Integration & ARMv7 (CRITICAL)

### Task 5.1: GCC Compilation Pipeline
**Goal:** Automate C → ARMv7 Assembly via GCC

**New File:** `src/backend.py`

**Features:**
- Generate C file from code generator
- Invoke GCC with proper flags
- Target ARMv7-A architecture
- Generate assembly output (.s files)
- Optional: Generate executable

**GCC Commands:**
```bash
# Compile to assembly
arm-linux-gnueabihf-gcc -S -march=armv7-a -mfloat-abi=hard input.c -o output.s

# Compile to executable (optional)
arm-linux-gnueabihf-gcc -march=armv7-a -mfloat-abi=hard input.c -o output

# For x86-64 testing:
gcc -S -O2 input.c -o output.s
```

**Estimated Time:** 4-6 hours

---

### Task 5.2: Build System Integration
**Goal:** Complete pipeline automation

**New File:** `build.py` or update `compile.py`

**Pipeline:**
```python
def compile_minipar_to_asm(source_file, output_asm):
    # 1. Lexical analysis
    tokens = lexer.tokenize(source)
    
    # 2. Syntax analysis
    ast = parser.parse(tokens)
    
    # 3. Semantic analysis
    semantic_analyzer.check(ast)
    
    # 4. TAC generation
    tac = codegen.generate(ast)
    
    # 5. C code generation
    c_code = c_codegen.generate(tac)
    
    # 6. Write C file
    with open('output.c', 'w') as f:
        f.write(c_code)
    
    # 7. Compile with GCC
    subprocess.run([
        'arm-linux-gnueabihf-gcc', '-S', 
        '-march=armv7-a', '-mfloat-abi=hard',
        'output.c', '-o', output_asm
    ])
```

**Estimated Time:** 3-5 hours

---

## 📋 Phase 6: Testing & Validation

### Task 6.1: Create Test Programs
**Goal:** Comprehensive test suite for 2025.1 requirements

**Test Programs Needed:**
1. `test_seq.minipar` - Sequential execution
2. `test_par.minipar` - Parallel execution with threads
3. `test_functions.minipar` - Function calls and recursion
4. `test_channels_client.minipar` - Client channel
5. `test_channels_server.minipar` - Server channel
6. `test_types.minipar` - Type checking
7. `test_operators.minipar` - All operators
8. `test_control_flow.minipar` - If/while/break/continue
9. `test_complex.minipar` - Complex program combining features

**Estimated Time:** 8-12 hours

---

### Task 6.2: Cross-Compilation Testing
**Goal:** Verify ARMv7 assembly output

**Setup:**
- Install ARM cross-compiler: `sudo apt-get install gcc-arm-linux-gnueabihf`
- QEMU for ARM emulation: `sudo apt-get install qemu-user`
- Test execution: `qemu-arm ./program`

**Estimated Time:** 4-6 hours

---

## 📊 Complete Timeline

| Phase | Tasks | Time | Priority |
|-------|-------|------|----------|
| Phase 1 | Bug fixes, SEQ/PAR, Methods | 10-14h | HIGH |
| Phase 2 | Semantic Analysis | 12-18h | CRITICAL |
| Phase 3 | Bytecode (Optional) | 14-20h | LOW |
| Phase 4 | C Code Generator | 26-42h | CRITICAL |
| Phase 5 | GCC Integration | 7-11h | CRITICAL |
| Phase 6 | Testing | 12-18h | HIGH |
| **Total (without Phase 3)** | **67-103h** | **3-5 weeks** |
| **Total (with Phase 3)** | **81-123h** | **4-6 weeks** |

**Recommended:** Skip Phase 3 (bytecode) for MVP - go directly TAC → C → GCC

---

## 🎯 Minimal Viable Product (MVP) Path

### Fast Track (2-3 weeks):
1. ✅ Fix bugs (Task 1.1-1.4) - 1 day
2. ✅ Semantic analysis (Task 2.1-2.2) - 3-4 days
3. ✅ C code generator (Task 4.1-4.3) - 5-7 days
4. ✅ GCC integration (Task 5.1-5.2) - 2 days
5. ✅ Testing (Task 6.1-6.2) - 2-3 days

**Total:** 13-17 working days

---

## 🔄 Development Workflow

### For Each Feature:
1. **Design** - Plan the implementation
2. **Implement** - Write the code
3. **Test** - Unit tests
4. **Integrate** - Add to pipeline
5. **Validate** - End-to-end test
6. **Document** - Update docs

### Git Workflow:
```bash
git checkout -b feature/semantic-analyzer
# ... implement ...
git add .
git commit -m "feat: add semantic analyzer with type checking"
git checkout main
git merge feature/semantic-analyzer
```

---

## 📚 Key Design Decisions

### 1. Skip Bytecode for MVP ✅
**Reason:** Direct TAC → C translation is simpler and faster
**Trade-off:** Less optimization opportunity, but GCC handles that

### 2. Use GCC for Assembly Generation ✅
**Reason:** Mature, optimized, supports many architectures
**Trade-off:** Dependency on external tool, but widely available

### 3. Stack-based TAC ✅
**Reason:** Current TAC is already three-address, easy to translate
**Trade-off:** None, works well for C generation

### 4. pthread for Parallelism ✅
**Reason:** Standard, portable, well-documented
**Trade-off:** Some platform limitations, but acceptable

### 5. BSD sockets for Channels ✅
**Reason:** Standard networking API, works on all POSIX systems
**Trade-off:** Requires network setup, but that's the requirement

---

## ✅ Success Criteria

### Phase 1 Complete When:
- [ ] All bugs fixed
- [ ] SEQ blocks parse and generate code
- [ ] PAR blocks parse and generate code
- [ ] Object method calls work

### Phase 2 Complete When:
- [ ] Symbol table tracks all symbols with scopes
- [ ] Type checking catches type errors
- [ ] Semantic errors reported clearly
- [ ] All test programs pass semantic analysis

### Phase 4 Complete When:
- [ ] TAC converts to valid C code
- [ ] Generated C compiles with gcc
- [ ] Programs execute correctly
- [ ] Threads work for PAR blocks
- [ ] Sockets work for channels

### Phase 5 Complete When:
- [ ] C code compiles to ARMv7 assembly
- [ ] Assembly can be assembled and linked
- [ ] Programs run on ARM (QEMU or hardware)
- [ ] Full pipeline automated

### Project Complete When:
- [ ] All 2025.1 requirements met
- [ ] All test programs work end-to-end
- [ ] Documentation complete
- [ ] Code quality maintained
- [ ] Performance acceptable

---

## 🚦 Current Status

**Completed:** ✅ Lexer, Parser, AST, TAC Generator (40%)

**In Progress:** ⏳ Requirements Analysis, Planning (5%)

**Next:** 🎯 Phase 1 - Bug Fixes & Foundation (0%)

**Overall Progress:** 45% complete

---

**Last Updated:** January 2025  
**Target Completion:** March 2025 (MVP) / April 2025 (Full)
