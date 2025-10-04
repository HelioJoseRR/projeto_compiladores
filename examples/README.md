# Exemplos de Código MiniPar

Esta pasta contém exemplos de programas escritos na linguagem MiniPar, demonstrando os principais recursos e a sintaxe da linguagem.

## 📝 Sintaxe da Linguagem MiniPar

### Declaração de Variáveis

```minipar
var nome: tipo = valor
```

Exemplos:
```minipar
var x: number = 10
var nome: string = "João"
var ativo: bool = true
var lista: list = []
var dados: dict = {}
```

### Declaração de Funções

```minipar
func nome_funcao(parametro1: tipo1, parametro2: tipo2) -> tipo_retorno {
    # corpo da função
    return valor
}
```

Exemplos:
```minipar
func soma(a: number, b: number) -> number {
    return a + b
}

func saudacao(nome: string) -> void {
    print("Olá,", nome)
}

# Parâmetros com valores padrão
func multiplicar(x: number, y: number = 2) -> number {
    return x * y
}
```

### Tipos de Dados

- `number`: Números inteiros e reais
- `string`: Cadeias de caracteres
- `bool`: Valores booleanos (`true` ou `false`)
- `void`: Tipo vazio (apenas para retorno de funções)
- `list`: Listas/arrays
- `dict`: Dicionários/mapas
- `any`: Qualquer tipo
- `c_channel`: Canal de comunicação cliente (sockets)
- `s_channel`: Canal de comunicação servidor (sockets)

### Estruturas de Controle

#### If-Else
```minipar
if (condicao) {
    # código
} else {
    # código alternativo
}
```

#### While
```minipar
while (condicao) {
    # código
    if (alguma_condicao) {
        break      # sai do loop
    }
    if (outra_condicao) {
        continue   # pula para próxima iteração
    }
}
```

### Comentários

```minipar
# Comentário de linha única

/* 
 * Comentário
 * de múltiplas
 * linhas
 */
```

### Operadores

#### Aritméticos
- `+` (adição)
- `-` (subtração)
- `*` (multiplicação)
- `/` (divisão)
- `%` (módulo)

#### Relacionais
- `==` (igual)
- `!=` (diferente)
- `<` (menor)
- `>` (maior)
- `<=` (menor ou igual)
- `>=` (maior ou igual)

#### Lógicos
- `&&` (e lógico)
- `||` (ou lógico)
- `!` (negação)

### Funções Built-in

- `print(...)`: Imprime valores
- `input(mensagem)`: Lê entrada do usuário
- `len(colecao)`: Retorna tamanho de uma coleção
- `to_string(valor)`: Converte valor para string

### Canais de Comunicação

```minipar
# Canal servidor
s_channel servidor {funcao, descricao, "host", porta}

# Canal cliente
c_channel cliente {"host", porta}
var resposta: string = cliente.send(mensagem)
cliente.close()
```

### Execução Paralela

```minipar
par {
    funcao1()
    funcao2()
}
```

## 📚 Descrição dos Exemplos

### ex1.minipar
**Conceitos demonstrados:**
- Declaração de variáveis com tipos
- Definição de funções com parâmetros e retorno
- Estruturas de controle (while, if)
- Chamadas de função
- Break em loops
- Comentários simples e compostos

```minipar
var a: number = 10
var b: bool = true

func soma(num1: number, num2: number) -> number {
    var s: number = num1 + num2
    while(a < 20) {
        a = a + 1
        print(a)
        if(a == 15) { break }
    }
    return s + 10
}

print(soma(2, 3))
```

### ex2.minipar
**Conceitos demonstrados:**
- Operadores relacionais e lógicos
- Valores padrão em parâmetros
- Conversão de tipos (to_string)
- Canais de servidor (s_channel)
- Loop infinito com break

```minipar
var a: bool = true
var b: bool = 1 >= 2
var c: number = -1

while(true) {
    break
}

func soma(num1: number = 0, num2: number) -> string {
    return to_string(num1 + num2)
}

print(soma(1,2))
var desc: string = "Digite dois numeros"
s_channel calculadora_server {soma, desc, "localhost", 1234}
```

### ex3.minipar
**Conceitos demonstrados:**
- Loops while com condições
- Múltiplas chamadas de print
- Funções com múltiplos parâmetros
- Expressões aritméticas complexas
- Função input para entrada do usuário
- Comentários de múltiplas linhas

### ex4.minipar
**Conceitos demonstrados:**
- Funções aninhadas (função dentro de função)
- Escopo de variáveis
- Execução paralela com `par`
- Múltiplas funções
- Loops while dentro de funções
- Função sleep (simulação de delay)

```minipar
func fatorial(x: number, y: number) -> void {
    func fat(n: number) -> number {
        var prod: number = 1
        var i: number = 2
        while(i <= n) {
            prod = prod * i
            i = i + 1
        }
        return prod
    }
    
    var i: number = x
    while(i <= y) {
        print("Fatorial de:", i, "=", fat(i))
        i = i + 1
        sleep(0.5)
    }
}

func fibonacci(n: number) -> void {
    var a: number = 0
    var b: number = 1
    var count: number = 0
    
    while (count < n) {
        print("Fib:", a)
        var aux: number = a + b
        a = b
        b = aux
        count = count + 1
        sleep(0.5)
    }
}

par {
    fatorial(2, 5)
    fibonacci(10)
}
```

### ex5.minipar
**Conceitos demonstrados:**
- Funções simples com parâmetros
- Decremento em loops
- Condições de parada

### fatorial_rec.minipar
**Conceitos demonstrados:**
- Recursão
- Estruturas if-else
- Operadores lógicos (||)
- Múltiplas condições

```minipar
func fatorial(n: number) -> number {
    if (n == 0 || n == 1) {
        return 1
    } else {
        return n * fatorial(n - 1)
    }
}

print("CALCULA O FATORIAL RECURSIVO")
var valor: number = 10
print("Fatorial: ", fatorial(valor))
```

### quicksort.minipar
**Conceitos demonstrados:**
- Algoritmo de ordenação recursivo
- Manipulação de listas
- Compreensão de lista (list comprehension)
- Métodos de lista (append, split, strip)
- Entrada e processamento de dados
- Estruturas de dados complexas

### recomendacao.minipar
**Conceitos demonstrados:**
- Dicionários complexos
- Iteração sobre dicionários e listas
- Funções matemáticas (pow, sqrt, sum)
- Sistema de recomendação completo
- Manipulação de estruturas de dados aninhadas
- Algoritmos de cálculo de similaridade
- Interface de texto interativa

### client.minipar
**Conceitos demonstrados:**
- Canais cliente (c_channel)
- Comunicação via sockets
- Loop de interação com usuário
- Condição de saída
- Envio e recebimento de mensagens
- Fechamento de conexão

```minipar
c_channel client {"localhost", 8585}

while(true) {
    var entrada: string = input("Digite uma expressão: ")
    if (entrada == "exit") {
        break
    }
    var ret: string = client.send(entrada)
    print(ret)
}

client.close()
```

## 🚀 Como Executar

Para compilar qualquer exemplo:

```bash
# Usando Python diretamente
python compile.py examples/ex1.minipar

# Ou usando UV (recomendado)
uv run compile.py examples/ex1.minipar

# Mostrar tokens durante compilação
python compile.py examples/ex1.minipar --tokens

# Mostrar AST durante compilação
python compile.py examples/ex1.minipar --ast

# Mostrar ambos
python compile.py examples/ex1.minipar --tokens --ast
```

## 📖 Notas Importantes

1. **Sem Ponto e Vírgula**: A linguagem MiniPar não requer ponto e vírgula (`;`) no final das declarações.

2. **Tipagem Explícita**: Todas as variáveis e parâmetros devem ter tipos declarados explicitamente.

3. **Anotação de Tipo**: Usa-se `:` para anotação de tipo e `->` para tipo de retorno de funções.

4. **Indentação**: Embora não seja obrigatória como em Python, uma boa indentação melhora a legibilidade.

5. **Extensão de Arquivo**: Use `.minipar` como extensão para arquivos da linguagem MiniPar.

## 🎯 Recursos Avançados

### Compreensão de Lista
```minipar
var quadrados: list = [for (var i: number in numeros) -> i * i]
```

### Métodos de String
```minipar
var texto: string = "  exemplo  "
var limpo: string = texto.strip()
var partes: list = texto.split(" ")
```

### Métodos de Lista
```minipar
var lista: list = [1, 2, 3]
lista.append(4)
var tamanho: number = len(lista)
```

### Operações com Dicionários
```minipar
var pessoa: dict = {"nome": "João", "idade": 25}
var chaves: list = pessoa.keys()
var valores: list = pessoa.values()
var itens: list = pessoa.items()
```

## 🔧 Dicas de Programação

1. **Sempre declare o tipo**: Isso ajuda na detecção de erros e melhora a legibilidade.
   
2. **Use nomes descritivos**: Prefira `contador` a `c`, `resultado` a `r`.

3. **Comente código complexo**: Especialmente algoritmos e lógicas não óbvias.

4. **Teste incrementalmente**: Compile e teste pequenas partes do código antes de adicionar mais funcionalidades.

5. **Verifique os tipos**: Certifique-se de que os tipos nas operações são compatíveis.

## 📚 Recursos de Aprendizado

Para aprender mais sobre a linguagem MiniPar:
- Consulte a [documentação principal](../README.md)
- Estude os exemplos fornecidos
- Experimente modificar os exemplos existentes
- Crie seus próprios programas

## 🤝 Contribuindo

Sinta-se à vontade para adicionar novos exemplos que demonstrem recursos interessantes da linguagem!

## ⚠️ Recursos Não Implementados (Atualmente)

Alguns dos exemplos mais avançados utilizam recursos que ainda não foram implementados no compilador:

1. **Métodos de Objetos** (`object.method()`): Exemplos como `client.minipar` que usam `client.send()` e `client.close()` ainda não são suportados.

2. **Execução Paralela** (`par { }`): O construto `par` para execução paralela (ex4.minipar) ainda não foi implementado.

3. **List Comprehension Avançada**: Compreensões de lista complexas (quicksort.minipar, recomendacao.minipar) ainda não são totalmente suportadas.

4. **Dicionários e Métodos de Coleções**: Operações avançadas com dicionários e métodos como `.keys()`, `.values()`, `.items()`, `.append()`, etc.

5. **Slicing de Listas**: Operações como `array[1:]` para obter sublistas.

6. **Funções Built-in Avançadas**: Funções como `pow()`, `sqrt()`, `sum()`, `intersection()`, `sort()`, `contains()`, etc.

### Exemplos que Compilam com Sucesso

Os seguintes exemplos compilam e geram código intermediário corretamente:
- ✅ **ex1.minipar** - Variáveis, funções, loops e controle de fluxo
- ✅ **ex2.minipar** - Declarações de canais e tipos básicos
- ✅ **ex3.minipar** - Loops while, if-else e entrada de usuário
- ✅ **ex5.minipar** - Funções simples com parâmetros
- ✅ **fatorial_rec.minipar** - Recursão e estruturas de controle

### Exemplos com Recursos Não Implementados

Estes exemplos contêm sintaxe válida MiniPar mas requerem recursos ainda não implementados:
- ⚠️ **ex4.minipar** - Usa `par { }` para execução paralela
- ⚠️ **client.minipar** - Usa métodos de objetos (`client.send()`)
- ⚠️ **quicksort.minipar** - Usa list comprehension e métodos de lista
- ⚠️ **recomendacao.minipar** - Usa dicionários, métodos de coleções e funções built-in avançadas
