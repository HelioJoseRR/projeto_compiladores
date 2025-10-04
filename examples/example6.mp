# Example 6: Complex program with nested control flow

func number gcd(number a, number b) {
    /* Calcula o máximo divisor comum
       usando o algoritmo de Euclides */
    while (b != 0) {
        number temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

func bool isPrime(number n) {
    if (n <= 1) {
        return false;
    }
    
    if (n == 2) {
        return true;
    }
    
    if (n % 2 == 0) {
        return false;
    }
    
    number i = 3;
    while (i * i <= n) {
        if (n % i == 0) {
            return false;
        }
        i = i + 2;
    }
    
    return true;
}

func void main() {
    number a = 48;
    number b = 18;
    number result = gcd(a, b);
    
    number num = 17;
    bool prime = isPrime(num);
    
    if (prime && result > 0) {
        result = result + num;
    } else {
        result = result - 1;
    }
}
