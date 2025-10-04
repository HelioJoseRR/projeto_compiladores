# Example 6: Programa complexo com algoritmos

/* Este exemplo demonstra:
   - Algoritmo de Euclides (GCD)
   - Teste de primalidade
   - Loops aninhados implicitamente
   - Lógica complexa
   - Uso integrado de todos os tipos
*/

func number gcd(number a, number b) {
    /* Máximo Divisor Comum usando algoritmo de Euclides */
    while (b != 0) {
        number temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

func number lcm(number a, number b) {
    /* Mínimo Múltiplo Comum */
    number divisor = gcd(a, b);
    return (a * b) / divisor;
}

func bool isPrime(number n) {
    /* Teste de primalidade */
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

func number power(number base, number exp) {
    /* Calcula base^exp */
    number result = 1;
    number i = 0;
    
    while (i < exp) {
        result = result * base;
        i = i + 1;
    }
    
    return result;
}

func number fibonacci(number n) {
    /* N-ésimo número de Fibonacci */
    if (n <= 1) {
        return n;
    }
    
    number a = 0;
    number b = 1;
    number i = 2;
    
    while (i <= n) {
        number temp = a + b;
        a = b;
        b = temp;
        i = i + 1;
    }
    
    return b;
}

func bool isPerfectSquare(number n) {
    /* Verifica se n é um quadrado perfeito */
    number i = 1;
    
    while (i * i <= n) {
        if (i * i == n) {
            return true;
        }
        i = i + 1;
    }
    
    return false;
}

func void main() {
    # Teste GCD e LCM
    number a = 48;
    number b = 18;
    number divisor = gcd(a, b);
    number multiplo = lcm(a, b);
    
    # Teste de primalidade
    number num1 = 17;
    number num2 = 20;
    bool prime1 = isPrime(num1);
    bool prime2 = isPrime(num2);
    
    # Potências
    number pow2_10 = power(2, 10);
    number pow3_5 = power(3, 5);
    
    # Fibonacci
    number fib10 = fibonacci(10);
    number fib20 = fibonacci(20);
    
    # Quadrados perfeitos
    bool square1 = isPerfectSquare(16);
    bool square2 = isPerfectSquare(17);
    
    # Lógica combinada
    if (prime1 && divisor > 0) {
        number result = divisor + num1;
    } else {
        number result = divisor - 1;
    }
    
    # Uso de strings com números
    string description = "Mathematical operations";
    number operationCount = 5;
    bool successful = true;
}
