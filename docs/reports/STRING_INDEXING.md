# String Indexing - Quick Reference Guide

## Overview

String indexing allows you to access individual characters in a string using bracket notation `[index]`.

## Basic Syntax

```minipar
var text: string = "Hello"
var first_char: string = text[0]  # Returns "H"
```

## Features

### 1. Direct Indexing
```minipar
var message: string = "MiniPar"
print(message[0])  # M
print(message[1])  # i
print(message[6])  # r
```

### 2. Variable Index
```minipar
var text: string = "Hello"
var i: number = 2
print(text[i])  # l
```

### 3. Expression Index
```minipar
var word: string = "Programming"
var pos: number = 3
print(word[pos + 2])     # r (index 5)
print(word[pos * 2])     # a (index 6)
print(word[10 - 5])      # a (index 5)
```

### 4. In Loops
```minipar
var text: string = "Loop"
var i: number = 0

while (i < 4) {
    print(text[i])
    i = i + 1
}
# Output: L, o, o, p
```

### 5. In Functions
```minipar
func get_char(s: string, index: number) -> string {
    return s[index]
}

var result: string = get_char("Function", 4)
print(result)  # t
```

### 6. In Conditionals
```minipar
var word: string = "Test"

if (word[0] == "T") {
    print("Starts with T")
}
```

### 7. Nested in Expressions
```minipar
var s1: string = "ABC"
var s2: string = "DEF"
var combined: string = s1[0] + s2[0]
print(combined)  # AD
```

## Error Handling

### Out of Bounds
```minipar
var text: string = "Hi"
print(text[5])  # Error: String index out of range: 5
```

### Non-Numeric Index
```minipar
var text: string = "Hello"
var idx: string = "invalid"
# Compile-time error: Index must be number, got string
```

## Common Patterns

### Get First Character
```minipar
var first: string = text[0]
```

### Get Last Character (manual)
```minipar
var text: string = "Hello"
var last: string = text[4]  # For 5-character string
```

### Iterate Through String
```minipar
var text: string = "Iterate"
var i: number = 0

while (i < 7) {  # Length of string
    print(text[i])
    i = i + 1
}
```

### Character Comparison
```minipar
func starts_with(text: string, prefix: string) -> bool {
    return text[0] == prefix[0]
}
```

### Extract Substring (manual)
```minipar
func get_chars(text: string, start: number, length: number) -> string {
    var result: string = ""
    var i: number = 0
    
    while (i < length) {
        result = result + text[start + i]
        i = i + 1
    }
    
    return result
}
```

## Type Information

- **Input**: String to index
- **Index**: Must be `number` type
- **Return**: Single character as `string`
- **Range**: 0 to (length - 1)

## TAC Generation

The compiler generates efficient Three-Address Code:

```minipar
var text: string = "Test"
var ch: string = text[2]
```

Generates:
```
0: text = "Test"
1: t0 = text[2]
2: ch = t0
```

## Best Practices

1. **Check Bounds**: Ensure index is within valid range
2. **Use Variables**: Store frequently accessed indices
3. **Clear Logic**: Make index calculations obvious
4. **Document**: Comment complex indexing expressions

## Examples

### Example 1: Character Counter
```minipar
func count_char(text: string, target: string) -> number {
    var count: number = 0
    var i: number = 0
    var length: number = 10  # Assume known length
    
    while (i < length) {
        if (text[i] == target) {
            count = count + 1
        }
        i = i + 1
    }
    
    return count
}
```

### Example 2: String Validator
```minipar
func is_valid_code(code: string) -> bool {
    # Check if code starts with 'X' and third char is digit
    if (code[0] != "X") {
        return false
    }
    
    var third: string = code[2]
    # Could check if third is digit
    
    return true
}
```

### Example 3: String Transformation
```minipar
func swap_first_last(text: string, length: number) -> string {
    if (length < 2) {
        return text
    }
    
    var first: string = text[0]
    var last: string = text[length - 1]
    
    # In real implementation, would rebuild string
    # This is simplified
    return last + first
}
```

## Limitations

Current implementation limitations:

1. **No Negative Indexing**: `-1` for last character not supported
2. **No Slicing**: `text[1:5]` not yet available
3. **Read-Only**: Cannot modify characters with `text[0] = "X"`
4. **Manual Length**: No built-in `len()` function yet (but it exists as builtin)

## Future Enhancements

Planned improvements:

- [ ] Negative indices for reverse access
- [ ] Slice notation `text[start:end]`
- [ ] String mutation support
- [ ] Range-based iteration
- [ ] List/Array indexing with same syntax

## See Also

- `BUG_FIXES.md` - Complete implementation details
- `examples/` - Example programs using indexing
- `QUICK_REFERENCE.md` - General language reference

---

**Version:** 2.1  
**Status:** ✅ Production Ready  
**Last Updated:** 2025-01-XX
