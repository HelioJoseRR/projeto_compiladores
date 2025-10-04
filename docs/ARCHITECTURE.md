# Arquitetura do Compilador Minipar

## Visão Geral

O compilador Minipar segue uma arquitetura clássica de compilador em três fases:

```
Código Fonte (.mp)
        ↓
   [LEXER] → Tokens
        ↓
   [PARSER] → AST
        ↓
  [CODEGEN] → Código de 3 Endereços
```

## Módulos Principais

### 1. lexer.py - Analisador Léxico

**Responsabilidades:**
- Ler o código fonte caractere por caractere
- Agrupar caracteres em tokens significativos
- Reconhecer palavras-chave, identificadores, operadores e literais
- Eliminar espaços em branco e comentários
- Reportar erros léxicos com posição precisa

**Classes Principais:**

#### `TokenType` (Enum)
Enumera todos os tipos de tokens possíveis na linguagem:
- Keywords: BREAK, CONTINUE, IF, WHILE, etc.
- Types: NUMBER, STRING, BOOL, VOID, etc.
- Operators: PLUS, MINUS, MULTIPLY, etc.
- Literals: NUMBER_LITERAL, STRING_LITERAL
- Delimiters: LPAREN, RPAREN, LBRACE, etc.

#### `Token` (Dataclass)
Representa um token individual:
- `type`: Tipo do token (TokenType)
- `value`: Valor associado ao token
- `line`: Linha onde o token aparece
- `column`: Coluna onde o token aparece

#### `Lexer` (Class)
Implementa o analisador léxico:

**Atributos:**
- `source`: Código fonte completo
- `pos`: Posição atual no código
- `line`, `column`: Posição atual (linha/coluna)
- `tokens`: Lista de tokens gerados

**Métodos Principais:**
- `tokenize()`: Método principal que gera todos os tokens
- `peek()`: Olha o próximo caractere sem consumir
- `advance()`: Consome e retorna o próximo caractere
- `skip_whitespace()`: Pula espaços em branco
- `skip_comment()`: Processa comentários
- `read_number()`: Lê números inteiros e reais
- `read_string()`: Lê strings literais
- `read_identifier()`: Lê identificadores e palavras-chave

**Padrão de Design:** State Machine implícita

---

### 2. ast_nodes.py - Definições da AST

**Responsabilidades:**
- Definir a estrutura de dados para a árvore sintática
- Prover classes para cada tipo de nó sintático

**Hierarquia de Classes:**

```
ASTNode (base)
├── Program
├── VarDecl
├── FuncDecl
├── Block
├── Statements
│   ├── IfStmt
│   ├── WhileStmt
│   ├── ReturnStmt
│   ├── BreakStmt
│   ├── ContinueStmt
│   └── ExprStmt
└── Expressions
    ├── Assignment
    ├── BinaryOp
    ├── UnaryOp
    ├── FuncCall
    ├── Variable
    └── Literals
        ├── NumberLiteral
        ├── StringLiteral
        └── BoolLiteral
```

**Padrão de Design:** Composite Pattern

---

### 3. parser.py - Analisador Sintático

**Responsabilidades:**
- Verificar se a sequência de tokens forma um programa válido
- Construir a Árvore de Sintaxe Abstrata (AST)
- Reportar erros sintáticos

**Classe Principal:** `Parser`

**Atributos:**
- `tokens`: Lista de tokens do lexer
- `pos`: Posição atual na lista de tokens

**Métodos Principais:**

#### Métodos Utilitários:
- `current()`: Retorna o token atual
- `peek()`: Olha tokens à frente
- `advance()`: Consome o token atual
- `match()`: Verifica se o token atual é de um tipo específico
- `consume()`: Consome um token esperado ou gera erro

#### Métodos de Parsing (Descendente Recursivo):

**Declarações:**
- `parse()`: Ponto de entrada, retorna Program
- `declaration()`: Processa declarações (variáveis ou funções)
- `func_declaration()`: Processa declaração de função
- `var_declaration()`: Processa declaração de variável
- `parameter()`: Processa parâmetro de função

**Comandos:**
- `statement()`: Processa comandos
- `block()`: Processa bloco de código
- `if_statement()`: Processa if-else
- `while_statement()`: Processa while
- `return_statement()`: Processa return
- `break_statement()`: Processa break
- `continue_statement()`: Processa continue
- `expression_statement()`: Processa expressão como comando

**Expressões (com precedência):**
- `expression()`: Ponto de entrada para expressões
- `assignment()`: Nível de precedência: atribuição
- `logical_or()`: Nível de precedência: ||
- `logical_and()`: Nível de precedência: &&
- `equality()`: Nível de precedência: == !=
- `comparison()`: Nível de precedência: < > <= >=
- `term()`: Nível de precedência: + -
- `factor()`: Nível de precedência: * / %
- `unary()`: Nível de precedência: ! -
- `call()`: Chamadas de função
- `primary()`: Literais e variáveis

**Padrão de Design:** Recursive Descent Parser

**Gramática Implementada:**

```
program        → declaration* EOF
declaration    → funcDecl | varDecl
funcDecl       → "func" type ID "(" parameters? ")" block
varDecl        → type ID ( "=" expression )? ";"
parameters     → parameter ( "," parameter )*
parameter      → type ID
block          → "{" statement* "}"
statement      → ifStmt | whileStmt | returnStmt | breakStmt
                | continueStmt | block | varDecl | exprStmt
ifStmt         → "if" "(" expression ")" statement ( "else" statement )?
whileStmt      → "while" "(" expression ")" statement
returnStmt     → "return" expression? ";"
breakStmt      → "break" ";"
continueStmt   → "continue" ";"
exprStmt       → expression ";"
expression     → assignment
assignment     → logical_or ( "=" assignment )?
logical_or     → logical_and ( "||" logical_and )*
logical_and    → equality ( "&&" equality )*
equality       → comparison ( ( "==" | "!=" ) comparison )*
comparison     → term ( ( "<" | ">" | "<=" | ">=" ) term )*
term           → factor ( ( "+" | "-" ) factor )*
factor         → unary ( ( "*" | "/" | "%" ) unary )*
unary          → ( "!" | "-" ) unary | call
call           → primary ( "(" arguments? ")" )?
primary        → NUMBER | STRING | "true" | "false" | ID | "(" expression ")"
```

---

### 4. codegen.py - Gerador de Código Intermediário

**Responsabilidades:**
- Gerar código de três endereços a partir da AST
- Gerenciar variáveis temporárias
- Gerenciar labels para controle de fluxo
- Manter tabela de símbolos

**Classes Principais:**

#### `TAC` (Three-Address Code)
Representa uma instrução de código intermediário:
- `op`: Operação (ADD, SUB, ASSIGN, GOTO, etc.)
- `arg1`: Primeiro argumento
- `arg2`: Segundo argumento
- `result`: Resultado

#### `CodeGenerator`
Implementa o gerador de código:

**Atributos:**
- `code`: Lista de instruções TAC geradas
- `temp_count`: Contador de temporários
- `label_count`: Contador de labels
- `symbol_table`: Tabela de símbolos (variável → tipo)

**Métodos Principais:**
- `generate()`: Método dispatcher que chama o método apropriado
- `new_temp()`: Gera nova variável temporária (t0, t1, ...)
- `new_label()`: Gera novo label (L0, L1, ...)
- `emit()`: Emite uma instrução TAC

**Métodos de Geração (um para cada tipo de nó AST):**
- `gen_Program()`: Gera código para o programa
- `gen_VarDecl()`: Gera código para declaração de variável
- `gen_FuncDecl()`: Gera código para função
- `gen_IfStmt()`: Gera código para if-else
- `gen_WhileStmt()`: Gera código para while
- `gen_BinaryOp()`: Gera código para operação binária
- `gen_UnaryOp()`: Gera código para operação unária
- `gen_FuncCall()`: Gera código para chamada de função
- etc.

**Padrão de Design:** Visitor Pattern (via dispatch dinâmico)

**Formato das Instruções TAC:**

| Instrução | Formato | Exemplo |
|-----------|---------|---------|
| Atribuição | `result = arg1` | `x = 10` |
| Binária | `result = arg1 op arg2` | `t0 = x + y` |
| Unária | `result = op arg1` | `t1 = - x` |
| Label | `LABEL arg1` | `LABEL L0` |
| Goto | `GOTO arg1` | `GOTO L1` |
| Condicional | `IF_FALSE arg1 GOTO result` | `IF_FALSE t0 GOTO L2` |
| Função | `FUNC_BEGIN arg1` | `FUNC_BEGIN main` |
| Parâmetro | `PARAM arg1` | `PARAM x` |
| Chamada | `CALL arg1 arg2 result` | `CALL foo 2 t5` |
| Retorno | `RETURN arg1` | `RETURN t3` |

---

### 5. compiler.py - Driver Principal

**Responsabilidades:**
- Interface de linha de comando
- Orquestrar as três fases do compilador
- Reportar erros e progresso
- Exibir resultados

**Funções Principais:**

#### `compile_source(source, show_tokens, show_ast)`
Compila código fonte em memória:
1. Cria instância do Lexer e gera tokens
2. Cria instância do Parser e gera AST
3. Cria instância do CodeGenerator e gera TAC
4. Exibe resultados conforme flags

#### `compile_file(filename, ...)`
Compila arquivo do disco

#### `main()`
Processa argumentos da linha de comando e chama compile_file

---

## Fluxo de Dados

```
┌─────────────────┐
│  example.mp     │  Arquivo fonte
└────────┬────────┘
         │ read
         ↓
┌─────────────────┐
│  source: str    │  String do código fonte
└────────┬────────┘
         │ Lexer.tokenize()
         ↓
┌─────────────────┐
│ tokens: [Token] │  Lista de tokens
└────────┬────────┘
         │ Parser.parse()
         ↓
┌─────────────────┐
│  ast: Program   │  Árvore Sintática Abstrata
└────────┬────────┘
         │ CodeGenerator.generate()
         ↓
┌─────────────────┐
│  code: [TAC]    │  Código de três endereços
└─────────────────┘
```

## Tratamento de Erros

### Erros Léxicos (Lexer)
- Caracteres inválidos
- Strings não terminadas
- Comentários não terminados

Exemplo:
```python
raise SyntaxError(f"Lexer error at {line}:{column}: {msg}")
```

### Erros Sintáticos (Parser)
- Tokens inesperados
- Estruturas inválidas
- Falta de delimitadores

Exemplo:
```python
raise SyntaxError(f"Parser error at {line}:{column}: {msg}")
```

## Extensibilidade

### Adicionar Novo Token
1. Adicione em `TokenType` enum
2. Adicione reconhecimento em `Lexer.tokenize()`
3. Se for keyword, adicione em `Lexer.KEYWORDS`

### Adicionar Nova Construção Sintática
1. Crie classe em `ast_nodes.py`
2. Adicione método de parsing em `parser.py`
3. Adicione método `gen_<ClassName>` em `codegen.py`

### Adicionar Nova Otimização
1. Crie novo módulo `optimizer.py`
2. Processe a lista de TAC antes de retornar
3. Implemente peephole, constant folding, etc.

## Decisões de Design

### Por que Python?
- Foco em simplicidade e legibilidade
- Dataclasses facilitam definição de nós AST
- Enums para tipos de tokens
- Sem overhead de tipos complexos

### Por que Recursive Descent?
- Simples de implementar e entender
- Fácil de debugar
- Boa correspondência com a gramática
- Não requer ferramentas externas

### Por que Três Endereços?
- Formato intermediário padrão
- Fácil de gerar e otimizar
- Próximo do assembly
- Boa base para backend

## Performance

### Complexidade Temporal
- Lexer: O(n) onde n = tamanho do código
- Parser: O(n) onde n = número de tokens
- CodeGen: O(m) onde m = número de nós na AST

### Complexidade Espacial
- Tokens: O(n)
- AST: O(n)
- TAC: O(n)

## Limitações

1. **Sem análise semântica**: Não verifica tipos, escopo, etc.
2. **Sem otimização**: Código intermediário não é otimizado
3. **Sem backend**: Não gera código de máquina
4. **Funções aninhadas**: Não suportadas
5. **Arrays**: Não implementados
6. **Structs**: Não implementados

## Possíveis Extensões Futuras

1. **Análise Semântica**
   - Type checking
   - Scope analysis
   - Symbol table completa

2. **Otimizações**
   - Constant folding
   - Dead code elimination
   - Common subexpression elimination

3. **Backend**
   - Geração de assembly
   - Geração de LLVM IR
   - Interpretador do TAC

4. **Recursos da Linguagem**
   - Arrays
   - Structs
   - Funções de primeira classe
   - Closures
   - Paralelismo (par keyword)

## Referências

- Aho, Sethi, Ullman - "Compilers: Principles, Techniques, and Tools" (Dragon Book)
- Cooper & Torczon - "Engineering a Compiler"
- Appel - "Modern Compiler Implementation"
