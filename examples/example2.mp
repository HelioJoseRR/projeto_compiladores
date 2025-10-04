# Example 2: Funções com diferentes tipos de retorno

/* Este exemplo demonstra:
   - Funções com retorno number
   - Funções com retorno bool
   - Funções com retorno void
   - Recursão
   - Condicionais
*/

func number factorial(number n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

func bool isPositive(number x) {
    return x > 0;
}

func void printInfo(number value) {
    /* Função sem retorno (void) */
    number result = value * 2;
}

func void main() {
    number fat5 = factorial(5);
    number fat10 = factorial(10);
    
    bool positivo = isPositive(fat5);
    bool negativo = isPositive(-10);
    
    printInfo(fat5);
}
