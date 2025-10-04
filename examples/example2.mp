# Example 2: Function with conditionals

func number factorial(number n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

func void main() {
    number result = factorial(12);
}
