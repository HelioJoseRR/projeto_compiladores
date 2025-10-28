# Quick Start Guide - Compilador Minipar

## 🚀 Início Rápido

### Opção 1: Com UV (Recomendado - Mais Rápido) ⚡

UV é um gerenciador de pacotes Python extremamente rápido.

#### 1. Instalar UV

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Alternativa (qualquer sistema):**
```bash
pip install uv
```

#### 2. Sincronizar Projeto

```bash
uv sync
```

Isso irá:
- ✅ Criar ambiente virtual em `.venv`
- ✅ Instalar o projeto
- ✅ Configurar tudo automaticamente

#### 3. Usar o Compilador

```bash
# Compilar programa
uv run compiler.py example1.mp

# Executar testes
uv run test_compiler.py

# Com flags de debug
uv run compiler.py example2.mp --tokens --ast
```

📖 **Guia completo do UV**: [UV_GUIDE.md](UV_GUIDE.md)

---

### Opção 2: Método Tradicional (Python)

#### 1. Verificar Instalação do Python

```bash
py --version
```

Se não tiver Python instalado, baixe em: https://www.python.org/downloads/

**Nota**: Este projeto não tem dependências externas - usa apenas a biblioteca padrão!

#### 2. Testar o Compilador

Execute os testes para garantir que tudo está funcionando:

```bash
py test_compiler.py
```

Você deve ver:
```
✅ All tests passed successfully!
```

#### 3. Compilar Seu Primeiro Programa

Crie um arquivo `hello.mp`:

```minipar
func void main() {
    number x = 10;
    number y = 20;
    number sum = x + y;
}
```

Compile:

```bash
py compiler.py hello.mp
```

#### 4. Ver Todos os Detalhes

Para ver o processo completo de compilação:

```bash
py compiler.py hello.mp --tokens --ast
```

## 📚 Próximos Passos

### Explorar os Exemplos

O projeto inclui 6 exemplos prontos:

```bash
# Exemplo 1: Aritmética básica
py compiler.py example1.mp

# Exemplo 2: Recursão (Fatorial)
py compiler.py example2.mp

# Exemplo 3: Loop while
py compiler.py example3.mp

# Exemplo 4: Lógica booleana
py compiler.py example4.mp

# Exemplo 5: Strings
py compiler.py example5.mp

# Exemplo 6: Programa complexo (GCD e Prime)
py compiler.py example6.mp
```

### Escrever Seu Próprio Código

Sintaxe básica da linguagem Minipar:

```minipar
# Declaração de variáveis
number x = 10;
string nome = "Maria";
bool ativo = true;

# Função
func number soma(number a, number b) {
    return a + b;
}

# Condicional
if (x > 0) {
    y = x * 2;
} else {
    y = 0;
}

# Loop
while (x < 10) {
    x = x + 1;
}
```

## 📖 Documentação Completa

- **README.md** - Visão geral do projeto
- **USAGE.md** - Guia detalhado de uso
- **ARCHITECTURE.md** - Arquitetura interna do compilador

## 🐛 Problemas Comuns

### Python não encontrado
```bash
# Use py ao invés de python:
py compiler.py arquivo.mp
```

### Erro de sintaxe no arquivo .mp
- Verifique se todas as instruções terminam com `;`
- Verifique se as strings têm `"` de abertura e fechamento
- Verifique se as chaves `{}` estão balanceadas

### Ver mensagens de erro detalhadas
O compilador mostra exatamente onde está o erro:
```
❌ Compilation Error: Parser error at 5:10: Expected ';' after variable declaration
```

## 💡 Dicas

1. Comece com exemplos simples
2. Use `--tokens` para entender a tokenização
3. Use `--ast` para visualizar a estrutura
4. Consulte USAGE.md para sintaxe completa
5. Execute test_compiler.py após mudanças

## 🎯 Estrutura do Projeto

```
projeto_compiladores/
├── lexer.py           # Análise Léxica
├── parser.py          # Análise Sintática
├── codegen.py         # Geração de Código
├── compiler.py        # Programa Principal
├── test_compiler.py   # Testes
├── example*.mp        # Exemplos
└── *.md              # Documentação
```

## 🏆 Recursos Suportados

✅ Tipos: number, string, bool, void, c_channel, s_channel
✅ Operadores: aritméticos, relacionais, lógicos
✅ Estruturas: if-else, while
✅ Funções: declaração, chamada, recursão
✅ Comentários: simples (#) e multi-linha (/* */)
✅ Código de três endereços (TAC)

## 📞 Ajuda Adicional

Se precisar de mais informações, consulte:
- Exemplos em `example*.mp`
- Testes em `test_compiler.py`
- Documentação completa em `USAGE.md`
- Arquitetura em `ARCHITECTURE.md`

---

**Pronto para começar!** 🎉

Execute: `py compiler.py example1.mp`
