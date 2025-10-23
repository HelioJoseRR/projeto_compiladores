# Bugs and Missing Features Found

## Summary
The compiler passes all basic tests but fails on 3 advanced example files due to missing language features.

## Bugs Found

### 1. **Array Indexing Not Supported** ❌
**Files affected:** `ex7.minipar`, `quicksort.minipar`
**Error:** `Parser error: Unexpected token: LBRACKET`

**Example:**
```minipar
message[index]  // ❌ Not supported
array[0]        // ❌ Not supported
```

**Fix needed:** Add LBRACKET handling in `call()` method after primary expression to support:
- `array[index]` - single element access
- `array[start:end]` - slicing (optional)

---

### 2. **List Comprehensions Not Supported** ❌
**Files affected:** `quicksort.minipar`
**Error:** `Parser error: Expected RPAREN`

**Example:**
```minipar
var array: list = [for (var n: string in numbers) -> n.to_number()]  // ❌ Not supported
```

**Fix needed:** Add list comprehension parsing in `primary()` when encountering `[for ...]`

---

### 3. **For-In Loops Not Supported** ❌
**Files affected:** `quicksort.minipar`
**Error:** Parser cannot handle `for (var x in array)` syntax

**Example:**
```minipar
for (var x: any in array[1:]) {  // ❌ Not supported
    if (x <= pivot) {
        menores.append(x)
    }
}
```

**Fix needed:** Add `for_in_statement()` method to parse:
```
for (var identifier : type in iterable) { statements }
```

---

### 4. **Method Call Return Type Inference** ⚠️
**Files affected:** `client.minipar`
**Error:** `Semantic error: Type mismatch: cannot assign void to string for variable 'ret'`

**Example:**
```minipar
var ret: string = client.send(entrada)  // send() inferred as void
```

**Issue:** Semantic analyzer doesn't properly infer return types for method calls on channel objects. It defaults to `void`.

**Fix needed:** Update semantic analyzer to:
- Track method signatures for channel types
- Infer return types based on method definitions
- Allow user-defined methods on channels

---

## Files Status

### ✅ Working Files (9/14)
- ex1.minipar - Variables, functions, control flow
- ex2.minipar - Server channels and types
- ex3.minipar - Loops and user input
- ex4.minipar - Parallel execution
- ex5.minipar - Simple functions
- ex8.minipar - Complex control flow
- ex9.minipar - Fibonacci
- fatorial_rec.minipar - Recursive factorial
- test_break_continue.minipar - Break/continue
- test_method_calls.minipar - Method calls
- test_seq_par.minipar - Sequential/parallel blocks
- test_semantic_errors.minipar - Error detection (intentional errors)

### ❌ Broken Files (3/14)
- **client.minipar** - Method return type issue
- **ex7.minipar** - Array indexing not supported
- **quicksort.minipar** - Array indexing, list comprehensions, for-in loops
- **recomendacao.minipar** - Unknown syntax (needs investigation)

---

## Priority Fixes

### High Priority
1. **Array indexing** - Core feature needed by multiple examples
2. **Method return types** - Semantic analysis bug

### Medium Priority  
3. **For-in loops** - Useful iteration feature
4. **List comprehensions** - Advanced feature

### Low Priority
5. Investigate `recomendacao.minipar` syntax requirements

---

## Testing Commands

Test all examples:
```bash
cd projeto_compiladores
Get-ChildItem examples\*.minipar | ForEach-Object { py compile.py $_.FullName }
```

Test specific file:
```bash
py compile.py examples\ex7.minipar
py compile.py examples\client.minipar
py compile.py examples\quicksort.minipar
```

Run full test suite:
```bash
py run_tests.py
```
