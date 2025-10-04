# Example 3: Loops e controle de fluxo

/* Este exemplo demonstra:
   - Loops while
   - Comandos break e continue
   - Acumuladores
   - Contadores
*/

func number sumWhile(number n) {
    number total = 0;
    number i = 1;
    
    while (i <= n) {
        total = total + i;
        i = i + 1;
    }
    
    return total;
}

func number sumEvenNumbers(number max) {
    number sum = 0;
    number i = 0;
    
    while (i <= max) {
        if (i % 2 == 0) {
            sum = sum + i;
        }
        i = i + 1;
    }
    
    return sum;
}

func number countDigits(number n) {
    number count = 0;
    
    while (n > 0) {
        count = count + 1;
        n = n / 10;
    }
    
    return count;
}

func void main() {
    number total = sumWhile(100);
    number pares = sumEvenNumbers(50);
    number digitos = countDigits(12345);
}
