# Example 3: While loop and control flow

func number sum(number n) {
    number total = 0;
    number i = 1;
    
    while (i <= n) {
        total = total + i;
        i = i + 1;
    }
    
    return total;
}

func void main() {
    number result = sum(10);
}
