# Example 4: Tipo bool e lógica booleana

/* Este exemplo demonstra:
   - Tipo bool (booleano)
   - Valores true e false
   - Operadores lógicos: &&, ||, !
   - Operadores relacionais
   - Expressões booleanas complexas
*/

func bool isEven(number x) {
    return x % 2 == 0;
}

func bool isOdd(number x) {
    return !isEven(x);
}

func bool inRange(number x, number min, number max) {
    return (x >= min) && (x <= max);
}

func bool isValidScore(number score) {
    /* Valida se o score está entre 0 e 100 */
    return (score >= 0) && (score <= 100);
}

func void main() {
    number a = 10;
    number b = 5;
    
    bool evenA = isEven(a);
    bool oddB = isOdd(b);
    bool result = (a > b) && evenA;
    
    # Operadores lógicos
    bool and_result = true && false;
    bool or_result = true || false;
    bool not_result = !true;
    
    # Expressões complexas
    bool complex = (a > b) && (isEven(a) || isOdd(b));
    bool range_check = inRange(a, 0, 100);
    
    if (result && complex) {
        a = a + 1;
    } else {
        b = b - 1;
    }
    
    # Validação de scores
    bool valid1 = isValidScore(85);
    bool valid2 = isValidScore(-5);
    bool valid3 = isValidScore(105);
}
