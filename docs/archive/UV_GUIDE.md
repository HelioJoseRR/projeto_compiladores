# Guia de Instalação com UV

## 🚀 Instalação Rápida com UV

Este projeto usa [UV](https://github.com/astral-sh/uv), um gerenciador de pacotes Python extremamente rápido.

### Passo 1: Instalar UV

#### Windows
```powershell
# Via pip
pip install uv

# Via PowerShell (recomendado)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Linux/macOS
```bash
# Via curl
curl -LsSf https://astral.sh/uv/install.sh | sh

# Via pip
pip install uv
```

### Passo 2: Sincronizar Dependências

```bash
# Clone o repositório (se ainda não fez)
git clone <seu-repositorio>
cd projeto_compiladores

# Sincronize as dependências (cria ambiente virtual automaticamente)
uv sync
```

**Pronto!** O UV irá:
- ✅ Criar um ambiente virtual (`.venv`)
- ✅ Instalar todas as dependências
- ✅ Configurar o projeto

### Passo 3: Usar o Compilador

#### Com UV Run (recomendado)
```bash
# Compilar um programa
uv run compiler.py example1.mp

# Executar testes
uv run test_compiler.py

# Com flags
uv run compiler.py example2.mp --tokens --ast
```

#### Ou Ativar o Ambiente Virtual
```bash
# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

# Depois usar normalmente
python compiler.py example1.mp
python test_compiler.py
```

## 📦 Comandos UV Úteis

### Gerenciamento de Dependências

```bash
# Sincronizar (instalar) dependências
uv sync

# Sincronizar apenas dependências de produção
uv sync --no-dev

# Adicionar nova dependência
uv add <pacote>

# Adicionar dependência de desenvolvimento
uv add --dev <pacote>

# Remover dependência
uv remove <pacote>

# Atualizar dependências
uv sync --upgrade
```

### Executar Comandos

```bash
# Executar script Python
uv run python script.py

# Executar comando no ambiente virtual
uv run <comando>

# Executar com argumentos
uv run compiler.py example1.mp --tokens
```

### Gerenciamento de Ambiente

```bash
# Criar ambiente virtual
uv venv

# Limpar cache do UV
uv cache clean

# Verificar instalação
uv --version
```

## 🎯 Por Que UV?

### Vantagens do UV

1. **⚡ Extremamente Rápido**
   - 10-100x mais rápido que pip
   - Resolução de dependências paralela
   - Cache inteligente

2. **🔒 Determinístico**
   - Lock file garantido (`uv.lock`)
   - Builds reproduzíveis
   - Sem surpresas

3. **🛠️ Moderno**
   - Escrito em Rust
   - Compatível com pip/pyproject.toml
   - Suporte a PEP 621

4. **📦 Tudo-em-um**
   - Gerenciador de pacotes
   - Gerenciador de ambiente virtual
   - Build tool

## 📋 Estrutura do Projeto

```
projeto_compiladores/
├── pyproject.toml    # Configuração do projeto (PEP 621)
├── uv.lock          # Lock file com dependências
├── .venv/           # Ambiente virtual (criado por uv sync)
├── lexer.py         # Código fonte
├── parser.py
├── codegen.py
├── compiler.py
├── test_compiler.py
└── ...
```

## 🔧 Configuração (pyproject.toml)

O arquivo `pyproject.toml` contém toda a configuração do projeto:

```toml
[project]
name = "minipar-compiler"
version = "1.0.0"
requires-python = ">=3.7"
dependencies = []  # Sem dependências externas!

[project.scripts]
minipar = "compiler:main"
minipar-test = "test_compiler:main"
```

### Scripts Definidos

Após `uv sync`, você pode usar:

```bash
# Executar compilador diretamente
uv run minipar example1.mp

# Executar testes diretamente
uv run minipar-test
```

## 🚨 Solução de Problemas

### UV não encontrado
```bash
# Reinstalar UV
pip install --upgrade uv

# Verificar PATH
which uv  # Linux/macOS
where uv  # Windows
```

### Erro ao sincronizar
```bash
# Limpar cache e tentar novamente
uv cache clean
rm -rf .venv  # ou rmdir /s .venv no Windows
uv sync
```

### Python não encontrado
```bash
# UV pode instalar Python automaticamente
uv python install 3.10

# Ou especificar versão
uv sync --python 3.10
```

### Ambiente virtual não funciona
```bash
# Recriar ambiente
rm -rf .venv
uv venv
uv sync
```

## 📚 Recursos Adicionais

- **Documentação UV**: https://docs.astral.sh/uv/
- **GitHub**: https://github.com/astral-sh/uv
- **PEP 621**: https://peps.python.org/pep-0621/

## 🔄 Migração de pip/poetry

### De requirements.txt

```bash
# UV pode ler requirements.txt
uv pip compile requirements.txt -o requirements.lock

# Ou migrar para pyproject.toml
# (já fizemos isso para você!)
```

### De poetry

```bash
# UV é compatível com pyproject.toml do Poetry
# Apenas execute:
uv sync
```

## ✨ Workflow Recomendado

### Para Usuários (apenas usar o compilador)

```bash
# 1. Clonar repositório
git clone <repo>
cd projeto_compiladores

# 2. Sincronizar (primeira vez)
uv sync

# 3. Usar compilador
uv run compiler.py seu_programa.mp
```

### Para Desenvolvedores (modificar código)

```bash
# 1. Clonar repositório
git clone <repo>
cd projeto_compiladores

# 2. Sincronizar com dev dependencies
uv sync --dev

# 3. Ativar ambiente virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/macOS

# 4. Desenvolver
python compiler.py example1.mp
python test_compiler.py

# 5. Commitar mudanças
git add .
git commit -m "suas mudanças"
```

## 🎓 Comparação de Comandos

| Tarefa | pip | poetry | uv |
|--------|-----|--------|-----|
| Instalar deps | `pip install -r requirements.txt` | `poetry install` | `uv sync` |
| Adicionar dep | `pip install <pkg>` | `poetry add <pkg>` | `uv add <pkg>` |
| Remover dep | `pip uninstall <pkg>` | `poetry remove <pkg>` | `uv remove <pkg>` |
| Executar script | `python script.py` | `poetry run python script.py` | `uv run script.py` |
| Lock deps | N/A | `poetry lock` | `uv lock` |
| Criar venv | `python -m venv .venv` | `poetry env use python` | `uv venv` |

## 💡 Dicas

1. **Sempre use `uv sync`** após clonar o repositório
2. **Use `uv run`** para garantir ambiente correto
3. **Commite `uv.lock`** para builds reproduzíveis
4. **Não commite `.venv/`** (já está no .gitignore)
5. **Use `uv cache clean`** se tiver problemas

## 🎯 Este Projeto

**Nota especial**: Este projeto **não tem dependências externas**!
- ✅ Usa apenas biblioteca padrão do Python
- ✅ Funciona com Python 3.7+
- ✅ Zero configuração necessária

O UV é opcional mas recomendado para:
- Gerenciamento consistente de ambiente
- Reprodutibilidade
- Performance

---

**Pronto para começar!**

```bash
uv sync
uv run compiler.py example1.mp
```
