# Compilador Minipar

Um compilador frontend completo para a linguagem Minipar, implementado em Python com foco em simplicidade e boas práticas de design.

## 📋 Estrutura do Projeto

```
projeto_compiladores/
├── src/                   # Código fonte do compilador
│   ├── __init__.py       # Inicialização do pacote
│   ├── lexer.py          # Análise Léxica (Tokenização)
│   ├── ast_nodes.py      # Definições dos nós da AST
│   ├── parser.py         # Análise Sintática (Parser)
│   ├── codegen.py        # Geração de Código Intermediário
│   └── compiler.py       # Driver principal do compilador
├── examples/             # Programas de exemplo em Minipar
│   ├── ex1.minipar       # Variáveis, funções e controle de fluxo
│   ├── ex2.minipar       # Canais de servidor e tipos
│   ├── ex3.minipar       # Loops e entrada de usuário
│   ├── ex4.minipar       # Funções aninhadas e execução paralela
│   ├── ex5.minipar       # Funções simples
│   ├── fatorial_rec.minipar  # Recursão
│   ├── quicksort.minipar     # Algoritmo de ordenação
│   ├── recomendacao.minipar  # Sistema de recomendação
│   ├── client.minipar        # Cliente de comunicação
│   └── README.md             # Documentação dos exemplos
├── tests/                # Testes do compilador
│   └── test_compiler.py  # Suite de testes
├── docs/                 # Documentação completa
│   ├── QUICKSTART.md
│   ├── USAGE.md
│   ├── ARCHITECTURE.md
│   ├── PROJECT_SUMMARY.md
│   ├── INDEX.md
│   ├── UV_GUIDE.md
│   ├── UV_QUICK_REFERENCE.md
│   └── UV_SETUP.md
├── compile.py            # Script para compilar (atalho)
├── run_tests.py          # Script para executar testes
├── minipar.py            # Ponto de entrada principal
├── pyproject.toml        # Configuração do projeto
├── uv.lock              # Lock file UV
└── README.md            # Este arquivo
```

## 🚀 Componentes do Compilador

### 1. Lexer (Análise Léxica)
- **Arquivo**: `lexer.py`
- **Função**: Converte código fonte em tokens
- **Características**:
  - Reconhece palavras-chave, identificadores, operadores e literais
  - Suporta comentários simples (#) e multi-linha (/* */)
  - Rastreamento preciso de linha e coluna para mensagens de erro
  - Tratamento de strings com escape sequences

### 2. Parser (Análise Sintática)
- **Arquivo**: `parser.py`
- **Função**: Constrói uma Árvore de Sintaxe Abstrata (AST)
- **Características**:
  - Parser recursivo descendente
  - Suporta precedência de operadores
  - Validação sintática completa
  - AST bem estruturada para facilitar a geração de código

### 3. Gerador de Código (Código Intermediário)
- **Arquivo**: `codegen.py`
- **Função**: Gera código de três endereços a partir da AST
- **Características**:
  - Instruções em formato de três endereços
  - Geração automática de variáveis temporárias
  - Geração de labels para controle de fluxo
  - Tabela de símbolos integrada

## 📦 Instalação e Uso

### Pré-requisitos
- Python 3.7 ou superior

### Método 1: Com UV (Recomendado) ⚡

[UV](https://github.com/astral-sh/uv) é um gerenciador de pacotes Python extremamente rápido.

```bash
# Instalar UV
pip install uv
# ou
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/macOS
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# Sincronizar dependências (cria .venv automaticamente)
uv sync

# Executar compilador
uv run compile.py examples/example1.mp

# Executar testes
uv run run_tests.py
```

**Vantagens do UV:**
- ⚡ 10-100x mais rápido que pip
- 🔒 Builds determinísticos com `uv.lock`
- 📦 Gerenciamento automático de ambiente virtual

📖 **Guia completo**: [docs/UV_GUIDE.md](docs/UV_GUIDE.md)

### Método 2: Tradicional com Python

```bash
# Executar compilador
python compile.py examples/ex1.minipar
# ou
py compile.py examples/ex1.minipar

# Executar testes
python run_tests.py
```

**Nota**: Este projeto **não tem dependências externas** - usa apenas a biblioteca padrão do Python!

### Executar o Compilador

```bash
# Compilar um arquivo Minipar
python compile.py examples/ex1.minipar

# Mostrar tokens durante compilação
python compile.py examples/ex1.minipar --tokens

# Mostrar AST durante compilação
python compile.py examples/ex1.minipar --ast

# Mostrar ambos
python compile.py examples/ex1.minipar --tokens --ast
```

### Executar Testes

```bash
python run_tests.py
```

## 📝 Exemplos de Código

### Example 1: Variáveis e Funções
```minipar
var a: number = 10
var b: bool = true

func soma(num1: number, num2: number) -> number {
    var s: number = num1 + num2
    return s + 10
}

print(soma(2, 3))
```

### Example 2: Função Recursiva (Fatorial)
```minipar
func fatorial(n: number) -> number {
    if (n == 0 || n == 1) {
        return 1
    } else {
        return n * fatorial(n - 1)
    }
}

var valor: number = 10
print("Fatorial: ", fatorial(valor))
```

### Example 3: Loop While
```minipar
var a: number = 10

while(a <= 15) {
    print("Contador:", a)
    a = a + 1
    if(a == 12) { break }
}

print("Final:", a)
```

### Example 4: Canais de Comunicação
```minipar
# Canal servidor
func soma(num1: number = 0, num2: number) -> string {
    return to_string(num1 + num2)
}

var desc: string = "Digite dois numeros"
s_channel calculadora_server {soma, desc, "localhost", 1234}

# Canal cliente
c_channel client {"localhost", 8585}
var entrada: string = input("Digite uma expressão: ")
var ret: string = client.send(entrada)
print(ret)
client.close()
```

## 🔧 Formato do Código de Três Endereços

O compilador gera código intermediário no formato de três endereços. Exemplos:

```
# Atribuição
x = 5

# Operação binária
t0 = x + y

# Operação unária
t1 = - x

# Controle de fluxo
IF_FALSE t0 GOTO L0
GOTO L1
LABEL L0

# Funções
FUNC_BEGIN factorial
PARAM n
RETURN t5
FUNC_END factorial

# Chamada de função
PARAM 5
CALL factorial 1 t10
```

## 🎯 Características da Linguagem Minipar

### Palavras-chave
- Controle de fluxo: `if`, `else`, `while`, `break`, `continue`, `return`
- Tipos: `number`, `string`, `bool`, `void`, `list`, `dict`, `any`, `c_channel`, `s_channel`
- Outros: `func`, `var`, `par`, `true`, `false`

### Sintaxe de Declarações

#### Variáveis
```minipar
var nome: tipo = valor
```

#### Funções
```minipar
func nome(param1: tipo1, param2: tipo2) -> tipo_retorno {
    # corpo
    return valor
}
```

### Operadores
- Aritméticos: `+`, `-`, `*`, `/`, `%`
- Relacionais: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Lógicos: `&&`, `||`, `!`
- Atribuição: `=`

### Tipos de Dados
- `number`: Inteiros e reais
- `string`: Cadeia de caracteres
- `bool`: Booleano (true/false)
- `void`: Tipo vazio (retorno de funções)
- `list`: Listas/arrays
- `dict`: Dicionários/mapas
- `any`: Qualquer tipo
- `func`: Tipo função
- `c_channel`: Canal socket cliente
- `s_channel`: Canal socket servidor

### Comentários
```minipar
# Comentário de linha única

/*
 * Comentário
 * de múltiplas linhas
 */
```

### Características Especiais
- **Sem ponto e vírgula**: As declarações não requerem `;` no final
- **Tipagem explícita**: Variáveis e parâmetros devem ter tipos declarados
- **Anotação de tipo**: Usa `:` para tipo de variável e `->` para tipo de retorno
- **Extensão de arquivo**: `.minipar`

## 🏗️ Arquitetura e Design

### Princípios Seguidos
1. **Separação de Responsabilidades**: Cada módulo tem uma função clara
2. **Simplicidade**: Código limpo e fácil de entender
3. **Extensibilidade**: Fácil adicionar novos recursos
4. **Tratamento de Erros**: Mensagens claras com linha e coluna

### Padrões de Projeto
- **Visitor Pattern** (implícito): Na geração de código
- **Strategy Pattern**: Diferentes métodos de geração para diferentes nós
- **Factory Pattern**: Geração de temporários e labels

## 🧪 Testes

O projeto inclui uma suite de testes abrangente que valida:
- Tokenização de diferentes construções
- Parsing de declarações e expressões
- Geração de código intermediário
- Compilação de programas completos

## 📚 Estrutura da AST

A AST é composta por nós que representam diferentes construções da linguagem:

- **Declarações**: `VarDecl`, `FuncDecl`
- **Comandos**: `IfStmt`, `WhileStmt`, `ReturnStmt`, `BreakStmt`, `ContinueStmt`
- **Expressões**: `BinaryOp`, `UnaryOp`, `FuncCall`, `Assignment`
- **Literais**: `NumberLiteral`, `StringLiteral`, `BoolLiteral`, `Variable`

## 🤝 Contribuindo

Para adicionar novos recursos:

1. **Novo token**: Adicione em `TokenType` e `Lexer.KEYWORDS` ou na lógica de tokenização
2. **Nova construção sintática**: Adicione o nó em `ast_nodes.py` e método de parsing em `parser.py`
3. **Geração de código**: Adicione método `gen_<NomeDaClasse>` em `codegen.py`

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte do curso de Compiladores.
