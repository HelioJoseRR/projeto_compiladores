# Guia de Uso do Compilador Minipar

## Introdução

Este compilador implementa o frontend completo para a linguagem Minipar, realizando as três principais fases:

1. **Análise Léxica (Lexer)**: Transforma o código fonte em tokens
2. **Análise Sintática (Parser)**: Constrói a Árvore de Sintaxe Abstrata (AST)
3. **Geração de Código Intermediário**: Produz código de três endereços

## Executando o Compilador

### Sintaxe Básica

```bash
py compiler.py <arquivo.minipar> [opções]
```

### Opções Disponíveis

- `--tokens`: Exibe o stream de tokens gerado pelo lexer
- `--ast`: Exibe a árvore sintática abstrata gerada pelo parser
- Ambas as opções podem ser combinadas

### Exemplos de Uso

```bash
# Compilação básica
py compiler.py example1.minipar

# Compilação com visualização de tokens
py compiler.py example1.minipar --tokens

# Compilação com visualização da AST
py compiler.py example2.minipar --ast

# Compilação com todas as informações
py compiler.py example3.minipar --tokens --ast
```

## Executando os Testes

Para verificar se o compilador está funcionando corretamente:

```bash
py test_compiler.py
```

Isso executará uma suite completa de testes que valida:
- Análise léxica de diferentes construções
- Análise sintática de declarações e expressões
- Geração de código intermediário
- Compilação de programas completos

## Estrutura do Código de Três Endereços

### Instruções de Atribuição

```
variavel = valor
variavel = expr1 op expr2
```

Exemplos:
```
x = 10
t0 = x + y
t1 = t0 * 2
```

### Instruções de Controle de Fluxo

```
LABEL Ln
GOTO Ln
IF_FALSE var GOTO Ln
IF_TRUE var GOTO Ln
```

Exemplos:
```
LABEL L0
t0 = x > 0
IF_FALSE t0 GOTO L1
GOTO L0
```

### Instruções de Função

```
FUNC_BEGIN nome_funcao
PARAM parametro
FUNC_END nome_funcao
CALL nome_funcao n_args resultado
RETURN valor
```

Exemplos:
```
FUNC_BEGIN factorial
PARAM n
RETURN t5
FUNC_END factorial
CALL factorial 1 t10
```

### Operações Unárias

```
resultado = op operando
```

Exemplos:
```
t0 = - x
t1 = ! flag
```

## Sintaxe da Linguagem Minipar

### Declaração de Variáveis

```minipar
number x = 10;
string nome = "Maria";
bool ativo = true;
```

### Declaração de Funções

```minipar
func tipo_retorno nome_funcao(tipo param1, tipo param2) {
    # corpo da função
    return valor;
}
```

Exemplo:
```minipar
func number soma(number a, number b) {
    return a + b;
}
```

### Estrutura Condicional (if-else)

```minipar
if (condicao) {
    # bloco then
} else {
    # bloco else (opcional)
}
```

Exemplo:
```minipar
if (x > 0) {
    y = x * 2;
} else {
    y = 0;
}
```

### Estrutura de Repetição (while)

```minipar
while (condicao) {
    # corpo do loop
}
```

Exemplo:
```minipar
number i = 0;
while (i < 10) {
    i = i + 1;
}
```

### Comandos de Controle

```minipar
return valor;    # Retorna valor da função
return;          # Retorna void
break;           # Interrompe loop
continue;        # Pula para próxima iteração
```

### Expressões

#### Operadores Aritméticos
- `+` Adição
- `-` Subtração
- `*` Multiplicação
- `/` Divisão
- `%` Módulo

#### Operadores Relacionais
- `==` Igual
- `!=` Diferente
- `<` Menor
- `>` Maior
- `<=` Menor ou igual
- `>=` Maior ou igual

#### Operadores Lógicos
- `&&` E lógico
- `||` OU lógico
- `!` Negação

#### Precedência de Operadores (da maior para menor)

1. Chamada de função: `func()`
2. Unários: `!`, `-`
3. Multiplicativos: `*`, `/`, `%`
4. Aditivos: `+`, `-`
5. Relacionais: `<`, `>`, `<=`, `>=`
6. Igualdade: `==`, `!=`
7. E lógico: `&&`
8. OU lógico: `||`
9. Atribuição: `=`

### Comentários

```minipar
# Comentário de linha única

/* Comentário
   de múltiplas
   linhas */
```

### Literais

```minipar
42          # número inteiro
3.14        # número real
"texto"     # string
true        # booleano verdadeiro
false       # booleano falso
```

## Mensagens de Erro

O compilador fornece mensagens de erro detalhadas incluindo:
- Tipo do erro (Lexer error ou Parser error)
- Linha e coluna onde o erro ocorreu
- Descrição do problema

Exemplo:
```
❌ Compilation Error: Lexer error at 5:10: Unexpected character: '@'
```

## Extensão de Arquivo

Use a extensão `.mp` (Minipar) para seus arquivos de código fonte.

## Limitações Conhecidas

1. Não há verificação de tipos (type checking) - apenas parsing
2. Não há otimização do código intermediário
3. Não há geração de código de máquina (apenas código intermediário)

## Exemplos Completos

### Exemplo 1: Fibonacci

```minipar
func number fibonacci(number n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

func void main() {
    number result = fibonacci(10);
}
```

### Exemplo 2: Máximo entre dois números

```minipar
func number max(number a, number b) {
    if (a > b) {
        return a;
    }
    return b;
}

func void main() {
    number x = 10;
    number y = 20;
    number maior = max(x, y);
}
```

### Exemplo 3: Fatorial iterativo

```minipar
func number factorial(number n) {
    number result = 1;
    number i = 1;
    
    while (i <= n) {
        result = result * i;
        i = i + 1;
    }
    
    return result;
}
```

## Dicas de Uso

1. **Use comentários** para documentar seu código
2. **Indente corretamente** para melhor legibilidade (embora não seja obrigatório)
3. **Declare variáveis no início** dos blocos quando possível
4. **Teste incrementalmente** compilando após cada modificação significativa
5. **Use o flag --tokens** para entender como o lexer tokeniza seu código
6. **Use o flag --ast** para visualizar a estrutura do programa

## Solução de Problemas

### Erro: "Unexpected character"
**Problema**: Caractere inválido no código fonte
**Solução**: Verifique se está usando apenas caracteres permitidos

### Erro: "Expected ';' after..."
**Problema**: Falta ponto e vírgula
**Solução**: Adicione `;` ao final da declaração

### Erro: "Unterminated string literal"
**Problema**: String não foi fechada com aspas
**Solução**: Adicione `"` para fechar a string

### Erro: "Expected type specifier"
**Problema**: Tipo não especificado na declaração
**Solução**: Adicione o tipo (number, string, bool, void, etc.)

## Recursos Adicionais

- Consulte o README.md para informações sobre a arquitetura
- Examine os arquivos example*.mp para mais exemplos
- Execute test_compiler.py para ver exemplos de uso da API
