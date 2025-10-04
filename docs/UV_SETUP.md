# UV Setup - Resumo da Configuração

## ✅ O Que Foi Configurado

Configurei o projeto para usar **UV (Ultraviolet)**, um gerenciador de pacotes Python moderno e extremamente rápido, escrito em Rust.

### 📦 Arquivos Criados

#### 1. `pyproject.toml`
Arquivo de configuração padrão Python (PEP 621) que define:
- Metadados do projeto (nome, versão, descrição)
- Compatibilidade com Python >= 3.7
- Scripts executáveis:
  - `minipar` → executa o compilador
  - `minipar-test` → executa os testes
- **Zero dependências externas** (usa apenas stdlib)

#### 2. `uv.lock`
Lock file que garante:
- Builds determinísticos
- Mesmas versões para todos
- Resolução de dependências otimizada
- **Commitar este arquivo no Git!**

#### 3. `.venv/` (criado por `uv sync`)
Ambiente virtual Python isolado:
- Criado automaticamente pelo UV
- Contém a instalação local do projeto
- **NÃO commitar** (já está no .gitignore)

#### 4. Documentação
- `UV_GUIDE.md` - Guia completo de uso (6.5 KB)
- `UV_QUICK_REFERENCE.md` - Referência rápida (5.9 KB)
- `README.md` - Atualizado com instruções UV
- `QUICKSTART.md` - Atualizado com opção UV
- `.gitignore` - Atualizado para ignorar `.venv/` e `.uv/`

## 🚀 Como Usar

### Setup Inicial (Uma Única Vez)

```bash
# Instalar UV (se ainda não tiver)
pip install uv

# Sincronizar projeto
uv sync
```

### Uso Diário

```bash
# Compilar programa
uv run compiler.py example1.mp

# Executar testes
uv run test_compiler.py

# Usando scripts definidos
uv run minipar example1.mp
uv run minipar-test

# Com flags de debug
uv run compiler.py example2.mp --tokens --ast
```

## 🎯 Vantagens do UV

### Performance
- ⚡ **10-100x mais rápido** que pip
- Resolução paralela de dependências
- Cache inteligente e reutilizável
- Instalação quase instantânea

### Confiabilidade
- 🔒 **Builds determinísticos** via uv.lock
- Garante mesmas versões em todos os ambientes
- Evita "funciona na minha máquina"
- Reprodução exata de ambientes

### Facilidade
- 📦 **Zero configuração** necessária
- Cria ambiente virtual automaticamente
- Compatível com pip e pyproject.toml padrão
- Funciona com qualquer projeto Python

### Modernidade
- 🦀 Escrito em **Rust** (seguro e rápido)
- Suporta PEP 621 (pyproject.toml moderno)
- Mantido pela Astral (criadores do Ruff)
- Comunidade ativa e crescente

## 📊 Comparação de Performance

| Operação | pip | poetry | uv |
|----------|-----|--------|-----|
| Primeira instalação | ~30s | ~25s | ~3s |
| Reinstalação (cache) | ~15s | ~12s | <1s |
| Resolução de deps | ~10s | ~8s | <1s |
| Criar venv | ~5s | ~3s | <1s |

*Tempos aproximados para projeto médio

## 🔄 Fluxo de Trabalho

### Para Novos Usuários

```bash
# 1. Clonar repositório
git clone <seu-repo>
cd projeto_compiladores

# 2. Instalar UV (primeira vez no sistema)
pip install uv

# 3. Sincronizar
uv sync

# 4. Usar
uv run compiler.py example1.mp
```

### Para Desenvolvedores

```bash
# Após clonar ou pull
uv sync  # Atualiza se necessário

# Desenvolver
uv run test_compiler.py  # Testar
uv run compiler.py example1.mp  # Testar manualmente

# Adicionar dependência (se necessário no futuro)
uv add <pacote>
git add pyproject.toml uv.lock
git commit -m "Add dependency"
```

### Para CI/CD

```yaml
# GitHub Actions exemplo
- name: Install UV
  run: pip install uv

- name: Sync dependencies
  run: uv sync

- name: Run tests
  run: uv run test_compiler.py
```

## 🎓 Comandos Essenciais

### Top 10 Comandos UV

```bash
# 1. Setup inicial
uv sync

# 2. Executar compilador
uv run compiler.py arquivo.mp

# 3. Executar testes
uv run test_compiler.py

# 4. Usar script definido
uv run minipar arquivo.mp

# 5. Adicionar dependência
uv add <pacote>

# 6. Remover dependência
uv remove <pacote>

# 7. Atualizar todas as deps
uv sync --upgrade

# 8. Limpar cache
uv cache clean

# 9. Reinstalar do zero
rm -rf .venv && uv sync

# 10. Ver versão
uv --version
```

## 📝 Notas Importantes

### O Que Commitar no Git

✅ **SIM - Commitar:**
- `pyproject.toml` - Configuração do projeto
- `uv.lock` - Lock file (garante reprodutibilidade)
- `UV_*.md` - Documentação
- Todo o código fonte

❌ **NÃO - Não Commitar:**
- `.venv/` - Ambiente virtual
- `__pycache__/` - Cache Python
- `.uv/` - Cache do UV
- `*.pyc` - Bytecode compilado

### Compatibilidade

✅ **Funciona com:**
- Python 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- Windows, Linux, macOS
- Qualquer projeto Python com pyproject.toml
- Projetos existentes com pip/poetry

✅ **Integra-se com:**
- Git/GitHub/GitLab
- CI/CD (Actions, Jenkins, etc.)
- Docker/containers
- IDEs (VSCode, PyCharm, etc.)

### Este Projeto Específico

💡 **Nota Especial:**
- **Zero dependências externas** - usa apenas stdlib
- UV é opcional mas recomendado
- Também funciona com `python` normal
- UV adiciona apenas conveniência e velocidade

## 🔍 Troubleshooting

### Problema: UV não encontrado
```bash
# Solução: Instalar/reinstalar
pip install --upgrade uv
```

### Problema: Erro ao sync
```bash
# Solução: Limpar e recriar
uv cache clean
rm -rf .venv
uv sync
```

### Problema: Script não funciona
```bash
# Solução: Verificar que sync foi executado
uv sync
uv run minipar example1.mp
```

### Problema: Python não encontrado
```bash
# Solução: UV pode instalar Python
uv python install 3.10
uv sync --python 3.10
```

## 📚 Recursos Adicionais

### Documentação do Projeto
- `UV_QUICK_REFERENCE.md` - Referência rápida de comandos
- `UV_GUIDE.md` - Guia completo de uso
- `README.md` - Visão geral do projeto
- `QUICKSTART.md` - Início rápido

### Recursos Externos
- **Site UV**: https://docs.astral.sh/uv/
- **GitHub UV**: https://github.com/astral-sh/uv
- **PEP 621**: https://peps.python.org/pep-0621/
- **Astral**: https://astral.sh/

## 🎉 Benefícios para Este Projeto

### Para Estudantes
- ✅ Setup instantâneo
- ✅ Mesma configuração para todos
- ✅ Menos problemas técnicos
- ✅ Foco no aprendizado

### Para Professores
- ✅ Distribuição fácil
- ✅ Ambiente consistente
- ✅ Menos suporte técnico
- ✅ Builds reproduzíveis

### Para Desenvolvimento
- ✅ Testes mais rápidos
- ✅ Iteração mais rápida
- ✅ Menor tempo de setup
- ✅ Mais produtividade

## 📈 Próximos Passos

### Opcional: Adicionar Dependências Futuras

Se no futuro você precisar adicionar dependências:

```bash
# Adicionar pacote
uv add <pacote>

# Exemplo: adicionar pytest
uv add --dev pytest

# Automaticamente atualiza:
# - pyproject.toml
# - uv.lock
```

### Opcional: Publicar no PyPI

```bash
# Build
uv build

# Publish (precisa configurar credenciais)
uv publish
```

## ✅ Checklist de Verificação

Marque se tudo está funcionando:

- [ ] `uv --version` mostra versão
- [ ] `uv sync` executa sem erros
- [ ] `.venv/` foi criado
- [ ] `uv run minipar example1.mp` funciona
- [ ] `uv run minipar-test` funciona
- [ ] `pyproject.toml` existe
- [ ] `uv.lock` existe
- [ ] Documentação UV existe

## 🏆 Status Final

✅ **UV configurado e funcionando**  
✅ **Lock file criado**  
✅ **Scripts definidos**  
✅ **Documentação completa**  
✅ **Testes passando**  
✅ **Pronto para uso**  

---

**Criado em:** Outubro 2025  
**Versão UV:** 0.5+  
**Python:** 3.7+  
**Status:** ✅ Completo

**Início rápido:**
```bash
uv sync
uv run compiler.py example1.mp
```
