# 📋 MiniPar 2025.1 - Requirements Analysis

**Date:** January 2025  
**Project Goal:** Complete compiler from MiniPar → Bytecode → C Code → GCC → ARMv7 Assembly

---

## 🎯 Project Requirements (2025.1)

### Pipeline Architecture
```
Código MiniPar → Lexer → Parser → AST → Semantic Analyzer → 
Symbol Table → Three-Address Code → Bytecode → C Code → GCC → ARMv7 Assembly
```

### Required Components (Software Components Architecture)

1. **✅ Lexical Analyzer (Lexer)** - IMPLEMENTED
2. **✅ Syntax Analyzer (Parser)** - IMPLEMENTED  
3. **❌ Semantic Analyzer** - NOT IMPLEMENTED
4. **⚠️ Symbol Table** - PARTIALLY (basic only)
5. **✅ Three-Address Code Generator** - IMPLEMENTED
6. **❌ Bytecode Generator** - NOT IMPLEMENTED
7. **❌ C Code Generator** - NOT IMPLEMENTED
8. **❌ ARMv7 Assembly Generator** - NOT IMPLEMENTED

---

## 📊 Current Implementation Status

### ✅ IMPLEMENTED (Excellent Quality)

#### 1. Lexer (lexer.py)
- ✅ All keywords recognized
- ✅ All operators (arithmetic, logical, relational)
- ✅ Comments (# and /* */)
- ✅ String literals with escapes
- ✅ Number literals (int and float)
- ✅ Identifiers and types
- ✅ Channel types (c_channel, s_channel)

#### 2. Parser (parser.py)
- ✅ Function declarations
- ✅ Variable declarations
- ✅ Control structures (if/else, while)
- ✅ Break, continue, return
- ✅ Expressions with precedence
- ✅ Function calls
- ✅ Channel declarations (syntax)

#### 3. AST Nodes (ast_nodes.py)
- ✅ Complete node hierarchy
- ✅ All statement types
- ✅ All expression types
- ✅ Channel declaration node

#### 4. Code Generator (codegen.py)
- ✅ Three-Address Code (TAC) generation
- ✅ Temporary variables
- ✅ Label generation
- ✅ Basic symbol table
- ✅ Function code generation
- ✅ Control flow generation

---

## ❌ MISSING IMPLEMENTATIONS (2025.1 Requirements)

### 1. Semantic Analyzer (CRITICAL - HIGH PRIORITY)

**What's Missing:**
- ❌ Type checking system
- ❌ Scope validation
- ❌ Undeclared variable detection
- ❌ Function signature validation
- ❌ Type compatibility checking
- ❌ Duplicate declaration detection

**Required:**
- Complete symbol table with scope management
- Type inference and checking
- Semantic error reporting
- Static analysis

**Estimated Effort:** 12-20 hours

---

### 2. SEQ and PAR Blocks (CRITICAL - HIGH PRIORITY)

**Current Status:** ❌ NOT IMPLEMENTED

**Required Syntax:**
```minipar
SEQ {
    # Sequential execution
    stmt1
    stmt2
}

PAR {
    # Parallel execution (threads)
    stmt1
    stmt2
}
```

**What Needs Implementation:**
- ❌ SEQ token in lexer
- ❌ PAR token in lexer (already exists but not used)
- ❌ Block statement parsing for SEQ/PAR
- ❌ AST nodes for SEQ and PAR blocks
- ❌ Code generation for threads (PAR)
- ❌ Thread management in bytecode/C generation

**Estimated Effort:** 8-12 hours

---

### 3. Channel Communication (MEDIUM PRIORITY)

**Current Status:** ⚠️ PARTIALLY IMPLEMENTED (syntax only)

**What Exists:**
- ✅ c_channel and s_channel syntax parsing
- ✅ Channel declaration in AST

**What's Missing:**
- ❌ Send operation
- ❌ Receive operation
- ❌ Socket implementation
- ❌ Network communication code generation

**Required Operations:**
```minipar
c_channel client {"localhost", 8080}
var data: string = client.receive()  # Missing
client.send("hello")  # Missing
client.close()  # Missing
```

**Estimated Effort:** 10-16 hours

---

### 4. Bytecode Generator (CRITICAL - HIGH PRIORITY)

**Current Status:** ❌ NOT IMPLEMENTED

**What's Needed:**
- Design bytecode instruction set
- Convert TAC to bytecode
- Bytecode serialization
- Bytecode optimization

**Bytecode Format Options:**
1. Stack-based (like JVM, Python bytecode)
2. Register-based (like Lua, Dalvik)
3. Custom format

**Estimated Effort:** 20-30 hours

---

### 5. C Code Generator (CRITICAL - HIGH PRIORITY)

**Current Status:** ❌ NOT IMPLEMENTED

**What's Needed:**
- Convert bytecode (or TAC) to C code
- Header generation
- Function translation
- Variable declarations
- Control flow mapping
- Thread support (pthread)
- Socket support (networking)

**Example Output:**
```c
#include <stdio.h>
#include <pthread.h>

int main() {
    int a = 10;
    int b = 20;
    int result = a + b;
    printf("%d\n", result);
    return 0;
}
```

**Estimated Effort:** 24-40 hours

---

### 6. ARMv7 Assembly Generator (CRITICAL - HIGH PRIORITY)

**Current Status:** ❌ NOT IMPLEMENTED

**What's Needed:**
- C code compilation to ARMv7 assembly
- Integration with GCC (arm-linux-gnueabihf-gcc)
- Register allocation
- Assembly instruction mapping
- System calls
- Linking

**GCC Command:**
```bash
gcc -S -march=armv7-a -mfloat-abi=hard input.c -o output.s
```

**Estimated Effort:** 30-50 hours (or use GCC directly)

---

### 7. Enhanced Symbol Table (MEDIUM PRIORITY)

**Current Status:** ⚠️ BASIC IMPLEMENTATION

**What Exists:**
- ✅ Simple dictionary mapping names to types

**What's Missing:**
- ❌ Scope hierarchy (global, function, block)
- ❌ Scope stack management
- ❌ Symbol properties (type, scope, line, is_initialized)
- ❌ Function symbol table (parameters, return type)
- ❌ Nested scope support
- ❌ Symbol lookup with scope resolution

**Estimated Effort:** 6-10 hours

---

### 8. Input/Output Operations (LOW PRIORITY)

**Current Status:** ⚠️ SYNTAX ONLY

**What's Missing:**
- ❌ Actual implementation of `input()`
- ❌ Proper `print()` with formatting
- ❌ File I/O operations

**Estimated Effort:** 4-6 hours

---

## 🔧 Grammar Updates Needed (2025.1)

### Current Grammar Gaps

**Missing Productions:**

```bnf
programa_minipar    → bloco_stmt
bloco_stmt          → bloco_SEQ | bloco_PAR
bloco_SEQ           → SEQ "{" stmts "}"
bloco_PAR           → PAR "{" stmts "}"
stmts               → stmt | stmt stmts
stmt                → atribuicao | if_stmt | while_stmt | func_call | 
                      return_stmt | break_stmt | continue_stmt | bloco_stmt
atribuicao          → ID "=" expr
if_stmt             → IF "(" expr ")" stmt (ELSE stmt)?
while_stmt          → WHILE "(" expr ")" stmt
func_decl           → FUNC ID "(" params? ")" "->" type bloco_stmt
var_decl            → VAR ID ":" type ("=" expr)?
c_channel           → C_CHANNEL ID "{" expr_list "}"
send_op             → ID "." SEND "(" expr ")"
receive_op          → ID "." RECEIVE "(" ")"
```

**Operator Precedence (Already Correct):**
1. Assignment (=)
2. Logical OR (||)
3. Logical AND (&&)
4. Equality (==, !=)
5. Comparison (<, >, <=, >=)
6. Addition/Subtraction (+, -)
7. Multiplication/Division/Modulo (*, /, %)
8. Unary (!, -)
9. Primary (literals, calls, variables)

---

## 🐛 Bug Analysis

### Critical Issues: NONE ✅

### Minor Issues Found:

1. **Break/Continue Code Generation Issue**
   - Location: codegen.py
   - Issue: Generates `None = None` for break/continue
   - Fix: Should generate proper GOTO to loop end/start labels
   - Priority: MEDIUM
   - Effort: 1-2 hours

2. **No Object Method Support**
   - Location: parser.py, ast_nodes.py
   - Issue: Cannot parse `obj.method()` syntax
   - Needed for: `client.send()`, `client.receive()`, `client.close()`
   - Priority: HIGH (required for channels)
   - Effort: 4-6 hours

3. **No For Loop Support**
   - Location: lexer.py, parser.py
   - Issue: Missing FOR keyword and parsing
   - Priority: LOW (while works)
   - Effort: 2-4 hours

4. **No List/Dict Operations**
   - Location: parser.py, codegen.py
   - Issue: No indexing, slicing, methods
   - Priority: MEDIUM
   - Effort: 8-12 hours

---

## 📈 Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
**Priority: CRITICAL**

1. **Semantic Analyzer** (12-20 hours)
   - Symbol table with scopes
   - Type checking
   - Semantic validation
   
2. **SEQ/PAR Blocks** (8-12 hours)
   - Lexer tokens
   - Parser grammar
   - AST nodes
   - Basic code generation

3. **Bug Fixes** (4-6 hours)
   - Break/continue generation
   - Object method parsing

**Deliverable:** Complete frontend with semantic analysis

---

### Phase 2: Code Generation (Week 3-4)
**Priority: HIGH**

4. **Bytecode Generator** (20-30 hours)
   - Design instruction set
   - TAC to bytecode conversion
   - Optimization

5. **C Code Generator** (24-40 hours)
   - Bytecode/TAC to C
   - Thread support (pthread)
   - I/O operations

**Deliverable:** Can generate C code from MiniPar

---

### Phase 3: Backend Integration (Week 5-6)
**Priority: HIGH**

6. **GCC Integration** (8-12 hours)
   - C compilation pipeline
   - ARMv7 target configuration
   - Build scripts

7. **Testing & Validation** (12-16 hours)
   - Test programs
   - Cross-compilation testing
   - Bug fixes

**Deliverable:** Complete compiler pipeline

---

### Phase 4: Advanced Features (Week 7-8)
**Priority: MEDIUM**

8. **Channel Communication** (10-16 hours)
   - Socket implementation
   - Send/receive operations
   - Network code generation

9. **Optimization** (12-20 hours)
   - Bytecode optimization
   - C code optimization
   - TAC optimization

**Deliverable:** Production-ready compiler

---

## 🎯 Minimum Viable Product (MVP)

To meet 2025.1 requirements, the MVP must include:

### Must Have (Critical):
- [x] Lexer
- [x] Parser  
- [x] AST
- [ ] Semantic Analyzer ⚠️
- [ ] Complete Symbol Table ⚠️
- [x] TAC Generator
- [ ] Bytecode Generator ⚠️
- [ ] C Code Generator ⚠️
- [ ] GCC Integration ⚠️
- [ ] ARMv7 Assembly Output ⚠️
- [ ] SEQ/PAR blocks ⚠️

### Should Have (High Priority):
- [ ] Type checking
- [ ] Channel operations (send/receive)
- [ ] Thread implementation (PAR)
- [ ] Object method calls
- [ ] Error handling throughout

### Nice to Have (Medium Priority):
- [ ] For loops
- [ ] List/dict operations
- [ ] Optimization passes
- [ ] Better error messages

---

## 📊 Effort Estimation Summary

| Component | Status | Effort |
|-----------|--------|--------|
| Semantic Analyzer | ❌ | 12-20h |
| SEQ/PAR Blocks | ❌ | 8-12h |
| Bytecode Generator | ❌ | 20-30h |
| C Code Generator | ❌ | 24-40h |
| GCC Integration | ❌ | 8-12h |
| Channel Operations | ⚠️ | 10-16h |
| Object Methods | ❌ | 4-6h |
| Symbol Table Enhancement | ⚠️ | 6-10h |
| Bug Fixes | ⚠️ | 4-6h |
| Testing | ⚠️ | 12-16h |
| **TOTAL** | | **108-168h** |

**Estimated Time:** 3-4 weeks full-time or 6-8 weeks part-time

---

## 🚀 Next Immediate Steps

### Step 1: Fix Current Bugs (Priority: IMMEDIATE)
1. Fix break/continue code generation
2. Add object method call support

### Step 2: Add SEQ/PAR Support (Priority: HIGH)
1. Add SEQ keyword to lexer
2. Update parser for block statements
3. Create AST nodes
4. Generate TAC for sequential/parallel execution

### Step 3: Implement Semantic Analysis (Priority: CRITICAL)
1. Design symbol table structure
2. Implement scope management
3. Add type checking
4. Integrate with parser

### Step 4: Build Code Generators (Priority: CRITICAL)
1. Design bytecode format
2. Implement TAC → Bytecode
3. Implement Bytecode → C
4. Test with GCC → ARMv7

---

## 📚 References

Based on "A Surprisingly Simple Lua Compiler" approach:
- Simple single-pass compilation
- Direct TAC to C translation (skip bytecode if simpler)
- Use GCC for optimization and assembly generation
- Focus on correctness over performance initially

**Alternative Approach:**
```
MiniPar → Lexer → Parser → AST → Semantic → TAC → C Code → GCC → ARMv7
```
Skip bytecode phase and go directly from TAC to C, using GCC for optimization.

---

## ✅ Conclusion

**Current State:** Excellent frontend (Lexer, Parser, TAC) - 40% complete

**To Complete:** Need semantic analysis, code generators, and GCC integration - 60% remaining

**Timeline:** 3-4 weeks full-time development

**Risk Level:** Low (good foundation, clear requirements)

**Recommendation:** Follow phased approach starting with semantic analysis and SEQ/PAR support

---

**Status:** ⚠️ IN PROGRESS - READY FOR NEXT PHASE  
**Last Updated:** January 2025
