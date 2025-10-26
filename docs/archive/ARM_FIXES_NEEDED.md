# ARM Assembly Generation - Critical Fixes Needed

## Issues Identified

Based on the error analysis in `armv7_errors.txt`, the following critical issues need to be fixed:

### 1. **Duplicate Label Conflicts** ❌
**Problem:** Labels like `L0`, `L1`, `L2` are reused across functions causing "Error: symbol L1 is already defined"

**Solution:**
```python
# In _generate_user_functions():
self.function_label_prefix = f"{func_name}_"

# In _make_unique_label():
def _make_unique_label(self, label: str) -> str:
    if self.function_label_prefix:
        return f"{self.function_label_prefix}{label}"
    return label

# When generating labels:
unique_label = self._make_unique_label("L0")  # becomes "soma_L0"
```

### 2. **Missing # Prefix for Immediates** ❌
**Problem:** `mov r0, 10` instead of `mov r0, #10`
**Error:** "Error: ARM register expected"

**Solution:**
```python
def _load_to_register(self, value, target_reg=None):
    # For numeric values
    try:
        num = int(float(str(value)))
        if target_reg:
            self.text_section.append(f"    mov {target_reg}, #{num}")  # ADD #
            return target_reg
    except:
        pass
```

### 3. **Direct Variable Use in Operations** ❌
**Problem:** `add r4, result, r4` where `result` is a variable name
**Error:** "Error: ARM register expected"

**Solution:**
```python
def _load_to_register(self, value, target_reg=None):
    # If it's a global variable
    if value in self.global_vars:
        if not target_reg:
            target_reg = self._get_temp_register()
        self.text_section.append(f"    ldr {target_reg}, ={value}")
        self.text_section.append(f"    ldr {target_reg}, [{target_reg}]")
        return target_reg
```

### 4. **String Literals Not in .rodata** ❌
**Problem:** Strings used directly in code
**Error:** Strings should be in read-only data section

**Solution:**
```python
def _analyze_tac(self, instructions):
    # Collect all string literals
    for instr in instructions:
        for value in [instr.arg1, instr.arg2, instr.result]:
            if value and isinstance(value, str) and value.startswith('"'):
                if value not in self.string_literals:
                    label = f".STR{self.string_counter}"
                    self.string_literals[value] = label
                    self.string_counter += 1

def _generate_rodata_section(self):
    if not self.string_literals:
        return
    
    self.rodata_section.append("    .section .rodata")
    self.rodata_section.append("    .align 2")
    for string_val, label in self.string_literals.items():
        clean_str = string_val[1:-1]  # Remove quotes
        self.rodata_section.append(f"{label}:")
        self.rodata_section.append(f'    .asciz "{clean_str}"')
```

### 5. **Division and Modulo Not Supported** ❌
**Problem:** ARM doesn't have direct `/` and `%` instructions
**Error:** Code generates incorrect assembly

**Solution:**
```python
if op == '/':
    # Load operands to r0, r1
    self.text_section.append(f"    mov r0, {left_reg}")
    self.text_section.append(f"    mov r1, {right_reg}")
    self.text_section.append(f"    bl __aeabi_idiv")  # Software division
    self.text_section.append(f"    mov {dest_reg}, r0")

if op == '%':
    self.text_section.append(f"    mov r0, {left_reg}")
    self.text_section.append(f"    mov r1, {right_reg}")
    self.text_section.append(f"    bl __aeabi_idivmod")  # Software modulo
    self.text_section.append(f"    mov {dest_reg}, r1")  # Remainder in r1
```

### 6. **Incorrect Parameter Handling** ❌
**Problem:** Parameters not loaded properly before function calls

**Solution:**
```python
if op == 'PARAM':
    if not hasattr(self, '_pending_params'):
        self._pending_params = []
    
    # Load parameter value to a register first
    param_reg = self._load_to_register(instr.arg1)
    self._pending_params.append(param_reg)
    return

if op == 'CALL':
    # Move parameters to r0-r3
    if hasattr(self, '_pending_params'):
        for i, param_reg in enumerate(self._pending_params[:4]):
            if not param_reg.startswith('r') or param_reg != f"r{i}":
                self.text_section.append(f"    mov r{i}, {param_reg}")
        self._pending_params = []
```

### 7. **Register Allocation Issues** ❌
**Problem:** Running out of registers, incorrect register tracking

**Solution:**
```python
def _allocate_register(self, var_name: str) -> str:
    if var_name in self.register_map:
        return self.register_map[var_name]
    
    # Use r4-r7 for locals
    if self.next_reg <= 7:
        reg = f"r{self.next_reg}"
        self.register_map[var_name] = reg
        self.next_reg += 1
        return reg
    
    # If out of registers, reuse r4
    return "r4"

def _get_temp_register(self) -> str:
    """Get a temporary register for intermediate values"""
    # Use r0-r3 for temps (caller-saved)
    return "r0"
```

### 8. **Function Epilogue Issues** ❌
**Problem:** Double epilogue (pop/bx lr appears twice)

**Solution:**
```python
# In _generate_user_functions():
# Only add epilogue if last instruction wasn't a return
if not (self.text_section and 'bx lr' in self.text_section[-1]):
    self.text_section.append("")
    self.text_section.append("    pop {r4, r5, r6, r7, lr}")
    self.text_section.append("    bx lr")
```

## Implementation Checklist

- [ ] Add function-specific label prefixes
- [ ] Always use # for immediate values
- [ ] Load variables from memory before operations
- [ ] Move strings to .rodata section
- [ ] Implement __aeabi_idiv and __aeabi_idivmod calls
- [ ] Fix parameter loading and passing
- [ ] Improve register allocation
- [ ] Fix function epilogue generation
- [ ] Add _start entry point symbol
- [ ] Handle string literals properly

## Testing Strategy

1. Test simple arithmetic: `ex5.minipar`
2. Test with functions: `ex1.minipar`
3. Test recursion: `fatorial_rec.minipar`, `ex9.minipar`
4. Test with strings: examples with print statements
5. Test modulo operation: `ex8.minipar`

## Expected Output Format

```armv7
    .data
var:    .word 0

    .section .rodata
    .align 2
.STR0:
    .asciz "Hello"

    .text
    .global main
    .align 2

main:
    push {r4, r5, r6, r7, lr}
    
    @ Load immediate correctly
    mov r0, #10  @ WITH #
    
    @ Load variable correctly
    ldr r1, =var
    ldr r1, [r1]  @ Load value from memory
    
    @ Call function
    bl func
    
    mov r0, #0
    pop {r4, r5, r6, r7, lr}
    bx lr

func:
    push {r4, r5, r6, r7, lr}
    @ Function body
    pop {r4, r5, r6, r7, lr}
    bx lr
    
    .end
```

## Reference

See `docs/tutorials/assembly.txt` for correct ARM assembly patterns.
