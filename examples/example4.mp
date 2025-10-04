# Example 4: Complex expressions and boolean logic

func bool isEven(number x) {
    return x % 2 == 0;
}

func void main() {
    number a = 10;
    number b = 5;
    bool result = (a > b) && isEven(a);
    
    if (result) {
        a = a + 1;
    } else {
        b = b - 1;
    }
}
