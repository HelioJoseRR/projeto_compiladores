# Exemplos Minipar

Esta pasta contém exemplos de código na linguagem Minipar, demonstrando todos os recursos e tipos suportados pelo compilador.

## 📝 Lista de Exemplos

### Example 1: Tipos Básicos e Aritmética
**Arquivo:** `example1.mp`

**Conceitos Demonstrados:**
- Declaração de variáveis com tipo `number`
- Números inteiros e reais (ponto flutuante)
- Operações aritméticas: `+`, `-`, `*`, `/`, `%`
- Operações compostas e precedência

**Código:**
```minipar
number inteiro = 10;
number real = 3.14;
number soma = inteiro + real;
number resultado = (inteiro + real) * produto - divisao;
```

**TAC Gerado:** 14 instruções

---

### Example 2: Funções com Diferentes Tipos de Retorno
**Arquivo:** `example2.mp`

**Conceitos Demonstrados:**
- Funções com retorno `number`
- Funções com retorno `bool`
- Funções com retorno `void` (sem retorno)
- Recursão (factorial)
- Estruturas condicionais (`if-else`)
- Passagem de parâmetros

**Código:**
```minipar
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
    number result = value * 2;
}
```

**TAC Gerado:** 41 instruções

---

### Example 3: Loops e Controle de Fluxo
**Arquivo:** `example3.mp`

**Conceitos Demonstrados:**
- Loop `while`
- Acumuladores e contadores
- Múltiplas funções
- Algoritmos: soma, contagem de dígitos, soma de pares

**Código:**
```minipar
func number sumWhile(number n) {
    number total = 0;
    number i = 1;
    
    while (i <= n) {
        total = total + i;
        i = i + 1;
    }
    
    return total;
}

func number countDigits(number n) {
    number count = 0;
    while (n > 0) {
        count = count + 1;
        n = n / 10;
    }
    return count;
}
```

**TAC Gerado:** 59 instruções

---

### Example 4: Tipo Bool e Lógica Booleana
**Arquivo:** `example4.mp`

**Conceitos Demonstrados:**
- Tipo `bool` (booleano)
- Valores `true` e `false`
- Operadores lógicos: `&&` (AND), `||` (OR), `!` (NOT)
- Operadores relacionais: `<`, `>`, `<=`, `>=`, `==`, `!=`
- Expressões booleanas complexas
- Validação de valores

**Código:**
```minipar
func bool isEven(number x) {
    return x % 2 == 0;
}

func bool inRange(number x, number min, number max) {
    return (x >= min) && (x <= max);
}

bool complex = (a > b) && (isEven(a) || isOdd(b));
```

**TAC Gerado:** 80 instruções

---

### Example 5: Tipo String e Múltiplos Tipos
**Arquivo:** `example5.mp`

**Conceitos Demonstrados:**
- Tipo `string` (cadeia de caracteres)
- Declaração de strings literais
- Passagem de strings como parâmetros
- Funções com múltiplos tipos de parâmetros
- Integração de `number`, `string` e `bool`

**Código:**
```minipar
func void greet(string name) {
    string greeting = "Hello, ";
}

func string getWelcomeMessage() {
    return "Welcome to Minipar!";
}

func void processUser(string username, number userId, bool active) {
    if (active) {
        string status = "Active";
    }
}
```

**TAC Gerado:** 49 instruções

---

### Example 6: Algoritmos Complexos
**Arquivo:** `example6.mp`

**Conceitos Demonstrados:**
- Algoritmo de Euclides (GCD - Máximo Divisor Comum)
- Cálculo de LCM (Mínimo Múltiplo Comum)
- Teste de primalidade
- Cálculo de potências
- Sequência de Fibonacci (iterativa)
- Verificação de quadrado perfeito
- Combinação de múltiplas funções

**Código:**
```minipar
func number gcd(number a, number b) {
    while (b != 0) {
        number temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

func bool isPrime(number n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    
    number i = 3;
    while (i * i <= n) {
        if (n % i == 0) return false;
        i = i + 2;
    }
    return true;
}

func number fibonacci(number n) {
    if (n <= 1) return n;
    
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
```

**TAC Gerado:** 165 instruções

---

### Example 7: Todos os Tipos da Linguagem Minipar
**Arquivo:** `example7.mp`

**Conceitos Demonstrados:**
- **TODOS os 7 tipos básicos** da linguagem Minipar:
  1. `number` - Números inteiros e reais
  2. `string` - Sequências de caracteres
  3. `bool` - Booleanos (true/false)
  4. `void` - Retorno vazio
  5. `func` - Tipo função
  6. `c_channel` - Canal socket cliente
  7. `s_channel` - Canal socket servidor
- Uso integrado de todos os tipos
- Declarações de funções com diferentes assinaturas

**Código:**
```minipar
# Tipo NUMBER
number inteiro = 42;
number real = 3.14159;

# Tipo STRING
string nome = "Alice";
string mensagem = "Hello, World!";

# Tipo BOOL
bool verdadeiro = true;
bool falso = false;

# Tipo FUNC (funções)
func number calcular(number x, number y) {
    return x * y + 10;
}

func bool verificar(number valor) {
    return valor > 0 && valor < 100;
}

func string formatar(string texto, number codigo) {
    return "Formatted";
}

func void processar(number n) {
    number temp = n * 2;
}

# Tipos CHANNEL
func void conectarCliente(c_channel canal) {
    number status = 1;
}

func void iniciarServidor(s_channel servidor) {
    number porta = 8080;
}
```

**TAC Gerado:** 101 instruções

---

## 🚀 Como Compilar os Exemplos

### Método 1: Script Auxiliar (Recomendado)
```bash
# Compilar um exemplo específico
python compile.py examples/example1.mp

# Com visualização de tokens
python compile.py examples/example1.mp --tokens

# Com visualização da AST
python compile.py examples/example2.mp --ast

# Com ambos
python compile.py examples/example3.mp --tokens --ast
```

### Método 2: Com UV
```bash
uv run compile.py examples/example1.mp
uv run compile.py examples/example4.mp --tokens --ast
```

### Método 3: Módulo Direto
```bash
python -m src.compiler examples/example1.mp
```

---

## 📊 Comparação dos Exemplos

| Exemplo | Tokens | Declarações | Instruções TAC | Complexidade |
|---------|--------|-------------|----------------|--------------|
| example1.mp | 52 | 7 | 14 | Básico |
| example2.mp | 109 | 4 | 41 | Médio |
| example3.mp | 163 | 4 | 59 | Médio |
| example4.mp | 228 | 5 | 80 | Médio-Alto |
| example5.mp | 176 | 5 | 49 | Médio |
| example6.mp | 466 | 7 | 165 | Alto |
| example7.mp | 329 | 19 | 101 | Alto |

---

## 🎯 Recursos Demonstrados por Exemplo

| Recurso | Ex1 | Ex2 | Ex3 | Ex4 | Ex5 | Ex6 | Ex7 |
|---------|-----|-----|-----|-----|-----|-----|-----|
| Tipo `number` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Tipo `string` | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Tipo `bool` | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Tipo `void` | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Tipo `func` | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Tipo `c_channel` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Tipo `s_channel` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Aritmética | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Lógica Booleana | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Condicionais | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Loops | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Recursão | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Múltiplas Funções | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 📖 Sugestão de Ordem de Estudo

Para aprender Minipar, recomendamos estudar os exemplos nesta ordem:

1. **example1.mp** - Comece aqui! Tipos básicos e aritmética
2. **example2.mp** - Aprenda sobre funções e recursão
3. **example3.mp** - Entenda loops e controle de fluxo
4. **example4.mp** - Domine lógica booleana
5. **example5.mp** - Trabalhe com strings
6. **example6.mp** - Aplique em algoritmos complexos
7. **example7.mp** - Veja todos os tipos juntos

---

## 🔍 Analisando o Código de Três Endereços (TAC)

Cada exemplo gera código intermediário no formato TAC. Para ver o código gerado:

```bash
python compile.py examples/example1.mp
```

Saída típica:
```
=== Three-Address Code ===
  0: inteiro = 10
  1: real = 3.14
  2: t0 = inteiro + real
  3: soma = t0
  ...
```

**Formato das instruções:**
- `var = valor` - Atribuição
- `t0 = x + y` - Operação binária
- `IF_FALSE t0 GOTO L1` - Salto condicional
- `LABEL L0` - Label (rótulo)
- `FUNC_BEGIN nome` - Início de função
- `CALL func n_args result` - Chamada de função

---

## ✅ Testes

Todos os exemplos são testados automaticamente:

```bash
python run_tests.py
```

Saída esperada:
```
Testing Full Examples...
  ✓ Basic types and arithmetic (example1.mp)
  ✓ Functions with different return types (example2.mp)
  ✓ Loops and control flow (example3.mp)
  ✓ Boolean logic and operations (example4.mp)
  ✓ String operations and multiple types (example5.mp)
  ✓ Complex algorithms (example6.mp)
  ✓ All Minipar types demonstration (example7.mp)
✅ Example tests completed!
```

---

## 💡 Dicas

1. **Comece simples**: Use example1.mp como base
2. **Experimente**: Modifique os exemplos e veja o TAC gerado
3. **Compare**: Veja como diferentes construções geram TAC diferente
4. **Debug**: Use `--tokens` e `--ast` para entender o processo
5. **Combine**: Crie seus próprios exemplos combinando conceitos

---

## 📚 Recursos Adicionais

- **Manual de Referência**: Consulte a especificação da linguagem
- **Documentação**: Veja `docs/` para mais informações
- **Arquitetura**: Leia `docs/ARCHITECTURE.md` para entender o compilador

---

**Última Atualização:** Outubro 2025  
**Status:** ✅ Todos os exemplos funcionando  
**Compatibilidade:** Python 3.7+, Windows/Linux/macOS
