# Índice do Projeto - Compilador Minipar

## 🎯 Para Começar Rapidamente

**Leia primeiro:** [QUICKSTART.md](QUICKSTART.md)

**Execute:**
```bash
py test_compiler.py              # Verificar instalação
py compiler.py example1.mp       # Primeiro programa
```

---

## 📚 Documentação por Objetivo

### Quero Aprender a Usar o Compilador
→ Comece com [QUICKSTART.md](QUICKSTART.md)  
→ Depois leia [USAGE.md](USAGE.md)  
→ Veja exemplos em `example*.mp`

### Quero Entender a Implementação
→ Leia [ARCHITECTURE.md](ARCHITECTURE.md)  
→ Depois [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)  
→ Estude o código em ordem:
   1. `ast_nodes.py` (estruturas de dados)
   2. `lexer.py` (análise léxica)
   3. `parser.py` (análise sintática)
   4. `codegen.py` (geração de código)

### Quero Modificar/Estender o Compilador
→ Leia [ARCHITECTURE.md](ARCHITECTURE.md) - seção "Extensibilidade"  
→ Execute `test_compiler.py` após cada mudança  
→ Veja `test_compiler.py` para exemplos de uso da API

### Quero Ver Exemplos de Código Minipar
→ Veja os arquivos `example*.mp`  
→ Compile com `py compiler.py example1.mp`  
→ Use `--tokens` e `--ast` para debug

---

## 📁 Guia Completo de Arquivos

### 🔧 Código Fonte (Ordem de Leitura Recomendada)

| Arquivo | Descrição | Linhas | Leia Para |
|---------|-----------|--------|-----------|
| `ast_nodes.py` | Definições dos nós da AST | 76 | Entender estruturas de dados |
| `lexer.py` | Analisador léxico | 322 | Entender tokenização |
| `parser.py` | Analisador sintático | 320 | Entender parsing |
| `codegen.py` | Gerador de código | 179 | Entender geração de TAC |
| `compiler.py` | Driver principal | 91 | Entender integração |
| `test_compiler.py` | Suite de testes | 217 | Ver exemplos de uso |

### 📝 Exemplos (Do Simples ao Complexo)

| Arquivo | Descrição | Conceitos |
|---------|-----------|-----------|
| `example1.mp` | Aritmética básica | Variáveis, operadores |
| `example2.mp` | Fatorial recursivo | Funções, recursão, if-else |
| `example3.mp` | Soma iterativa | While, loops |
| `example4.mp` | Lógica booleana | Operadores lógicos, bool |
| `example5.mp` | Strings | Strings, múltiplos tipos |
| `example6.mp` | GCD e Prime | Programa completo, nested loops |

### 📚 Documentação (Por Propósito)

| Arquivo | Para Quem | Conteúdo |
|---------|-----------|----------|
| `README.md` | Todos | Visão geral do projeto |
| `QUICKSTART.md` | Iniciantes | Início rápido, primeiros passos |
| `USAGE.md` | Usuários | Manual completo de uso |
| `ARCHITECTURE.md` | Desenvolvedores | Arquitetura interna |
| `PROJECT_SUMMARY.md` | Avaliadores | Resumo da implementação |
| `INDEX.md` | Todos | Este arquivo |

### 🔨 Outros Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `.gitignore` | Arquivos ignorados pelo Git |
| `__pycache__/` | Cache do Python (ignorar) |

---

## 🗺️ Mapa Mental do Projeto

```
COMPILADOR MINIPAR
│
├─ USAR O COMPILADOR
│  ├─ Início Rápido → QUICKSTART.md
│  ├─ Manual Completo → USAGE.md
│  └─ Exemplos → example*.mp
│
├─ ENTENDER O CÓDIGO
│  ├─ Arquitetura → ARCHITECTURE.md
│  ├─ Implementação → PROJECT_SUMMARY.md
│  └─ Código Fonte
│     ├─ AST → ast_nodes.py
│     ├─ Lexer → lexer.py
│     ├─ Parser → parser.py
│     ├─ CodeGen → codegen.py
│     └─ Main → compiler.py
│
├─ TESTAR
│  ├─ Suite de Testes → test_compiler.py
│  └─ Exemplos → example*.mp
│
└─ MODIFICAR/ESTENDER
   ├─ Guia → ARCHITECTURE.md (seção Extensibilidade)
   └─ Testes → test_compiler.py
```

---

## 🎓 Roteiros de Estudo

### Para Aprender Compiladores

**Dia 1: Fundamentos**
1. Leia QUICKSTART.md
2. Compile example1.mp e example2.mp
3. Entenda o output (TAC)

**Dia 2: Análise Léxica**
1. Leia seção Lexer em ARCHITECTURE.md
2. Estude lexer.py
3. Execute com --tokens

**Dia 3: Análise Sintática**
1. Leia seção Parser em ARCHITECTURE.md
2. Estude ast_nodes.py e parser.py
3. Execute com --ast

**Dia 4: Geração de Código**
1. Leia seção CodeGen em ARCHITECTURE.md
2. Estude codegen.py
3. Compare AST com TAC gerado

**Dia 5: Prática**
1. Escreva seu próprio programa .mp
2. Compile e analise o TAC
3. Modifique um exemplo

### Para Entender a Implementação

**Fase 1: Estruturas (30 min)**
- Leia ast_nodes.py completamente
- Entenda cada tipo de nó
- Desenhe a hierarquia

**Fase 2: Lexer (1 hora)**
- Leia lexer.py linha por linha
- Execute com --tokens em vários exemplos
- Teste com código inválido

**Fase 3: Parser (2 horas)**
- Leia parser.py
- Entenda precedência de operadores
- Execute com --ast em vários exemplos

**Fase 4: CodeGen (1 hora)**
- Leia codegen.py
- Trace a geração para example2.mp
- Entenda temporários e labels

**Fase 5: Integração (30 min)**
- Leia compiler.py
- Entenda o fluxo completo
- Execute test_compiler.py

### Para Modificar o Compilador

**Adicionar Novo Operador:**
1. Adicione TokenType em lexer.py
2. Adicione reconhecimento no lexer
3. Adicione no parser (precedência correta)
4. Adicione geração em codegen.py
5. Adicione teste em test_compiler.py
6. Teste com exemplo

**Adicionar Nova Estrutura de Controle:**
1. Adicione nó AST em ast_nodes.py
2. Adicione parsing em parser.py
3. Adicione geração em codegen.py
4. Adicione teste
5. Crie exemplo

**Adicionar Otimização:**
1. Crie novo módulo (ex: optimizer.py)
2. Processe TAC após geração
3. Adicione flag --optimize
4. Adicione testes comparativos

---

## 🔍 Busca Rápida

### Procurando Algo Específico?

**Como fazer X:**
- Adicionar tipo → ARCHITECTURE.md + lexer.py
- Adicionar operador → ARCHITECTURE.md + lexer.py + parser.py
- Adicionar comando → ast_nodes.py + parser.py + codegen.py
- Modificar TAC → codegen.py
- Adicionar teste → test_compiler.py

**Onde está X:**
- Palavras-chave → lexer.py (KEYWORDS)
- Precedência → parser.py (métodos de expressão)
- Geração de labels → codegen.py (new_label)
- Temporários → codegen.py (new_temp)
- Erros → Todos os arquivos (método error)

**Sintaxe de X:**
- Minipar → USAGE.md
- TAC → ARCHITECTURE.md ou codegen.py
- Comandos CLI → QUICKSTART.md
- Testes → test_compiler.py

---

## 💡 Dicas Importantes

### Para Estudantes
- ⭐ Comece pelos exemplos simples
- ⭐ Use --tokens e --ast para entender
- ⭐ Desenhe a AST no papel
- ⭐ Trace a execução manualmente

### Para Desenvolvedores
- ⭐ Rode test_compiler.py após mudanças
- ⭐ Mantenha separação de responsabilidades
- ⭐ Siga o padrão de nomeação existente
- ⭐ Adicione testes para novos recursos

### Para Professores
- ⭐ Use como exemplo de boa implementação
- ⭐ Exemplos graduados (simples → complexo)
- ⭐ Código comentado e documentado
- ⭐ Fácil de modificar e estender

---

## 📞 Perguntas Frequentes

**Q: Por onde começar?**  
A: QUICKSTART.md → exemplo1.mp → USAGE.md

**Q: Como funciona internamente?**  
A: ARCHITECTURE.md tem todos os detalhes

**Q: Posso modificar o código?**  
A: Sim! Veja seção Extensibilidade em ARCHITECTURE.md

**Q: Testes não passam, o que fazer?**  
A: Verifique instalação Python, encoding do console

**Q: Como adicionar recurso X?**  
A: Veja "Como Modificar" em ARCHITECTURE.md

---

## ✅ Checklist de Uso

Marque conforme avança:

### Primeiro Uso
- [ ] Leu QUICKSTART.md
- [ ] Executou test_compiler.py
- [ ] Compilou example1.mp
- [ ] Entendeu o output TAC

### Uso Básico
- [ ] Compilou todos os exemplos
- [ ] Usou --tokens
- [ ] Usou --ast
- [ ] Criou programa próprio

### Uso Avançado
- [ ] Leu ARCHITECTURE.md
- [ ] Entendeu o código fonte
- [ ] Modificou alguma funcionalidade
- [ ] Adicionou teste próprio

---

## 🚀 Comandos Rápidos

```bash
# Testar tudo
py test_compiler.py

# Compilar com detalhes
py compiler.py arquivo.mp --tokens --ast

# Ver apenas TAC
py compiler.py arquivo.mp

# Compilar todos exemplos
for %f in (example*.mp) do py compiler.py %f
```

---

**Navegação:**
- 🏠 [README.md](README.md) - Início
- 🚀 [QUICKSTART.md](QUICKSTART.md) - Início rápido  
- 📖 [USAGE.md](USAGE.md) - Manual completo
- 🏗️ [ARCHITECTURE.md](ARCHITECTURE.md) - Arquitetura
- 📊 [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Resumo

---

**Última atualização:** Outubro 2025  
**Versão:** 1.0.0  
**Status:** ✅ Completo e Funcional
