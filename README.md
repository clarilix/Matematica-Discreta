# Analisador de Lógica Proposicional

Projeto desenvolvido para a disciplina de **Matemática Discreta / Lógica Formal**  
Universidade Federal do Maranhão — UFMA  

Este programa recebe uma expressão lógica digitada pelo usuário e realiza
três tarefas automaticamente:

1. **Identifica** as proposições atômicas (p, q, r...) e os conectivos
   lógicos presentes na expressão (¬, ∧, ∨, →, ↔)
2. **Valida** se a expressão está escrita corretamente, rejeitando entradas
   inválidas ou mal formadas com mensagens de erro claras
3. **Gera a Tabela-Verdade completa** com 2ⁿ linhas — onde n é o número
   de proposições — e classifica a expressão como Tautologia,
   Contradição ou Contingência

---

##  Fundamentação Teórica

### Lógica Proposicional
A Lógica Proposicional é um ramo da Lógica Formal que estuda proposições —
afirmações que podem ser **Verdadeiras (V)** ou **Falsas (F)** — e as relações
entre elas através de conectivos lógicos.

### Proposições Atômicas
São as unidades básicas da lógica, representadas por letras minúsculas
(`p`, `q`, `r`, ...). Não podem ser decompostas em proposições menores.

### Conectivos Lógicos

| Conectivo | Símbolo | Notação no programa | Descrição |
|---|---|---|---|
| Negação | ¬ | `~p` | Inverte o valor lógico |
| Conjunção | ∧ | `p & q` | Verdadeiro só se ambos forem V |
| Disjunção | ∨ | `p \| q` | Verdadeiro se pelo menos um for V |
| Implicação | → | `p -> q` | Falso só quando p=V e q=F |
| Bicondicional | ↔ | `p <-> q` | Verdadeiro quando p e q têm o mesmo valor |

### Tabela-Verdade
A Tabela-Verdade lista todas as combinações possíveis de valores para as
proposições atômicas de uma expressão. Para `n` proposições, a tabela
possui **2ⁿ linhas**.

### Classificação das Expressões
- **Tautologia** → resultado Verdadeiro em todas as linhas
- **Contradição** → resultado Falso em todas as linhas
- **Contingência** → resultado varia conforme os valores das proposições

---


### Como cada módulo funciona

```
Você digita:  (p | q) -> r
                   ↓
     analisadorLexico.py  →  identifica os tokens (VAR, OU, IMPLICACAO...)
                   ↓
     analisadorSintatico.py  →  monta a Árvore Sintática Abstrata (AST)
                   ↓
     avaliador.py →  calcula V ou F para cada combinação
                   ↓
     tabela.py →  exibe a tabela completa + classificação
```

---

##  Instalação e Execução

### Pré-requisitos
- Python 3.8 ou superior instalado  
- Nenhuma biblioteca externa necessária (usa apenas `re` e `itertools`)

### Passo a passo

**1. Clone ou baixe o repositório:**
```bash
git clone https://github.com/seu-usuario/logica_proposicional.git
```

**2. Entre na pasta do projeto:**
```bash
cd logica_proposicional
```

**3. Execute o programa:**
```bash
python main.py
```

---

##  Formato de Entrada

O programa aceita expressões no seguinte formato:

| Operação | Como digitar | Exemplo |
|---|---|---|
| Negação | `~p` | `~p` |
| Conjunção | `p & q` | `p & q` |
| Disjunção | `p \| q` | `p \| q` |
| Implicação | `p -> q` | `p -> q` |
| Bicondicional | `p <-> q` | `p <-> q` |
| Parênteses | `(expr)` | `(p & q) -> r` |

>  **Atenção:** Use apenas letras simples para variáveis (`p`, `q`, `r`).  
> Espaços entre os elementos são opcionais mas recomendados.

---

##  Exemplos de Uso

### Exemplo 1 — Implicação simples
```
Digite a expressão: p -> q
```
```
  Proposições atômicas : p, q
  Linhas da tabela     : 2^2 = 4

  +───────+───────+────────+
  |   p   |   q   | p -> q |
  +═══════+═══════+════════+
  |   F   |   F   |   V    |
  |   F   |   V   |   V    |
  |   V   |   F   |   F    |
  |   V   |   V   |   V    |
  +───────+───────+────────+

  Classificação: CONTINGÊNCIA — 3× Verdadeiro, 1× Falso
```

### Exemplo 2 — Tautologia (Princípio do 3º Excluído)
```
Digite a expressão: p | ~p
```
```
  Classificação: ✔ TAUTOLOGIA — verdadeira para todas as interpretações
```

### Exemplo 3 — Contradição
```
Digite a expressão: p & ~p
```
```
  Classificação: ✘ CONTRADIÇÃO — falsa para todas as interpretações
```

### Exemplo 4 — Contraposição (3 variáveis)
```
Digite a expressão: (p -> q) <-> (~q -> ~p)
```
```
  Proposições atômicas : p, q
  Linhas da tabela     : 2^2 = 4
  Classificação: ✔ TAUTOLOGIA — verdadeira para todas as interpretações
```

### Exemplo 5 — Expressão com 3 variáveis
```
Digite a expressão: (p | q) -> r
```
```
  Proposições atômicas : p, q, r
  Linhas da tabela     : 2^3 = 8
  Classificação: CONTINGÊNCIA — 5× Verdadeiro, 3× Falso
```

---

##  Integrantes do Grupo

Tereza Clarice Rocha

##  Referências

- GERSTING, Judith L. *Fundamentos Matemáticos para a Ciência da Computação*. LTC, 2017.
- ROSEN, Kenneth H. *Matemática Discreta e suas Aplicações*. McGraw-Hill, 2009.
- SOUZA, Marco. *Lógica para Ciência da Computação*. Campus, 2008.
