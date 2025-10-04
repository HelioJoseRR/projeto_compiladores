# 🚀 Referência Rápida - Comandos UV

## Instalação

```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Via pip (qualquer sistema)
pip install uv
```

## Setup Inicial (Uma Vez)

```bash
# Sincronizar projeto (cria .venv automaticamente)
uv sync
```

## Uso Diário

### Compilar Programas

```bash
# Compilação básica
uv run compiler.py example1.mp

# Com visualização de tokens
uv run compiler.py example1.mp --tokens

# Com visualização da AST
uv run compiler.py example2.mp --ast

# Com todas as informações
uv run compiler.py example3.mp --tokens --ast
```

### Executar Testes

```bash
# Executar todos os testes
uv run test_compiler.py

# Ou usando script definido
uv run minipar-test
```

### Scripts Definidos (após uv sync)

```bash
# Compilador (atalho)
uv run minipar example1.mp

# Testes (atalho)
uv run minipar-test
```

## Comandos UV Essenciais

### Gerenciamento de Dependências

```bash
# Instalar/atualizar dependências
uv sync

# Adicionar nova dependência
uv add <pacote>

# Adicionar dep de desenvolvimento
uv add --dev <pacote>

# Remover dependência
uv remove <pacote>

# Atualizar todas as dependências
uv sync --upgrade

# Reinstalar tudo do zero
rm -rf .venv  # ou rmdir /s .venv no Windows
uv sync
```

### Executar Comandos

```bash
# Executar qualquer script Python
uv run python script.py

# Executar comando no ambiente
uv run <comando> [args...]

# Exemplo: executar com argumentos
uv run compiler.py example1.mp --tokens
```

### Gerenciamento de Ambiente

```bash
# Criar ambiente virtual manualmente
uv venv

# Especificar versão do Python
uv venv --python 3.10

# Limpar cache
uv cache clean

# Ver versão do UV
uv --version

# Ver ajuda
uv --help
```

### Python Versions

```bash
# Instalar Python via UV
uv python install 3.10

# Listar Pythons instalados
uv python list

# Usar versão específica
uv sync --python 3.10
```

## Comparação Rápida

| Tarefa | Comando Tradicional | Comando UV |
|--------|---------------------|------------|
| Instalar deps | `pip install -r requirements.txt` | `uv sync` |
| Executar script | `python script.py` | `uv run script.py` |
| Criar venv | `python -m venv .venv` | `uv venv` |
| Adicionar dep | `pip install pkg` | `uv add pkg` |
| Atualizar deps | `pip install --upgrade` | `uv sync --upgrade` |

## Dicas de Produtividade

### 1. Alias no Shell

**PowerShell** (adicione ao `$PROFILE`):
```powershell
function uvr { uv run @args }
function uvc { uv run compiler.py @args }
function uvt { uv run test_compiler.py }
```

**Bash/Zsh** (adicione ao `.bashrc`/`.zshrc`):
```bash
alias uvr='uv run'
alias uvc='uv run compiler.py'
alias uvt='uv run test_compiler.py'
```

Uso:
```bash
uvc example1.mp --tokens
uvt
```

### 2. Ativar Ambiente (Alternativa)

Se preferir ativar o ambiente manualmente:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows CMD
.venv\Scripts\activate.bat

# Linux/macOS
source .venv/bin/activate

# Depois pode usar python diretamente
python compiler.py example1.mp
```

### 3. Verificação Rápida

```bash
# Verificar se tudo está ok
uv sync && uv run test_compiler.py
```

## Estrutura de Arquivos

```
projeto_compiladores/
├── pyproject.toml      # Configuração do projeto
├── uv.lock            # Lock file (commitar!)
├── .venv/             # Ambiente virtual (NÃO commitar)
├── .gitignore         # Ignora .venv e __pycache__
└── *.py               # Código fonte
```

## Fluxo de Trabalho Típico

### Para Usuários (Primeiro Uso)

```bash
# 1. Clonar repositório
git clone <repo>
cd projeto_compiladores

# 2. Sincronizar (primeira vez)
uv sync

# 3. Usar compilador
uv run compiler.py example1.mp
```

### Para Desenvolvedores

```bash
# 1. Setup inicial
git clone <repo>
cd projeto_compiladores
uv sync

# 2. Fazer mudanças
# ... editar código ...

# 3. Testar
uv run test_compiler.py

# 4. Testar manualmente
uv run compiler.py example1.mp

# 5. Commitar (NÃO commitar .venv!)
git add .
git commit -m "suas mudanças"
git push
```

### Após Atualizar do Git

```bash
# Pull + sync
git pull
uv sync  # Atualiza deps se mudou pyproject.toml
```

## Solução Rápida de Problemas

### UV não encontrado
```bash
# Verificar instalação
which uv    # Linux/macOS
where uv    # Windows

# Reinstalar
pip install --upgrade uv
```

### Erro ao sincronizar
```bash
# Limpar e recriar
uv cache clean
rm -rf .venv
uv sync
```

### Python não encontrado
```bash
# UV pode instalar Python
uv python install 3.10
uv sync --python 3.10
```

### Ambiente quebrado
```bash
# Reset completo
rm -rf .venv .uv __pycache__
uv sync
```

## Por Que UV?

✅ **10-100x mais rápido** que pip  
✅ **Builds determinísticos** (uv.lock)  
✅ **Zero configuração** - funciona out-of-the-box  
✅ **Compatível com pip** - funciona com pyproject.toml padrão  
✅ **Moderno** - escrito em Rust, extremamente eficiente  

## Recursos

- 📖 **Documentação Completa**: [UV_GUIDE.md](UV_GUIDE.md)
- 🌐 **Site Oficial**: https://docs.astral.sh/uv/
- 💻 **GitHub**: https://github.com/astral-sh/uv
- 📚 **Docs do Projeto**: [README.md](README.md)

## Comandos Mais Usados (Top 5)

```bash
# 1. Setup inicial
uv sync

# 2. Compilar programa
uv run compiler.py arquivo.mp

# 3. Executar testes
uv run test_compiler.py

# 4. Compilar com debug
uv run compiler.py arquivo.mp --tokens --ast

# 5. Limpar e reinstalar
rm -rf .venv && uv sync
```

---

💡 **Dica**: Salve este arquivo como favorito para referência rápida!

🚀 **Início rápido**: `uv sync && uv run compiler.py example1.mp`
