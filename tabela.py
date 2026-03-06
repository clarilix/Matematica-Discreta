# tabela.py
from itertools import product
from analisadorLexico  import tokenizar, SIMBOLO_FORMAL
from analisadorSintatico import analisadorSintatico
from avaliador import avaliar, coletar_variaveis, coletar_conectivos


def exibir_tabela(formula_str: str):

    print("\n" + "═" * 62)
    print("  ANALISADOR DE LÓGICA PROPOSICIONAL")
    print("═" * 62)

    # Etapa 1: Tokenização
    tokens = tokenizar(formula_str)

    print(f"\n  Expressão : {formula_str}")
    print(f"\n  Tokens identificados:")
    print(f"    {'Tipo':<18} {'Valor':<8} Símbolo formal")
    print(f"    {'─'*18} {'─'*8} {'─'*14}")

    for tipo, val in tokens:
        simbolo = SIMBOLO_FORMAL.get(tipo, '—')
        print(f"    {tipo:<18} {val:<8} {simbolo}")

    # Etapa 2: Parse (AST)
    arvore = analisadorSintatico(tokens).parse()

    # Etapa 3: Proposições e conectivos
    variaveis  = sorted(coletar_variaveis(arvore))
    conectivos = coletar_conectivos(tokens)
    n          = len(variaveis)

    print(f"\n  Proposições atômicas : {', '.join(variaveis)}  ({n} no total)")
    print(f"  Conectivos           : {', '.join(conectivos) if conectivos else '(nenhum)'}")
    print(f"  Linhas da tabela     : 2^{n} = {2**n}")

    # Etapa 4: Tabela-Verdade
    cabecalho = variaveis + [formula_str]
    larguras  = [max(len(h), 5) for h in cabecalho]
    separador = "  +" + "+".join("─" * (w + 2) for w in larguras) + "+"
    formato   = "  |" + "|".join(f" {{:^{w}}} " for w in larguras) + "|"

    print(f"\n  Tabela-Verdade:\n")
    print(separador)
    print(formato.format(*cabecalho))
    print(separador.replace("─", "═"))

    resultados = []

    for combinacao in product([False, True], repeat=n):
        env       = dict(zip(variaveis, combinacao))
        resultado = avaliar(arvore, env)
        resultados.append(resultado)
        linha = ["V" if v else "F" for v in combinacao] + ["V" if resultado else "F"]
        print(formato.format(*linha))

    print(separador)

    # Etapa 5: Classificação
    total_V = resultados.count(True)
    total_F = resultados.count(False)

    if all(resultados):
        classe = "✔  TAUTOLOGIA   — verdadeira para TODAS as interpretações"
    elif not any(resultados):
        classe = "✘  CONTRADIÇÃO  — falsa para TODAS as interpretações"
    else:
        classe = f"◈  CONTINGÊNCIA — {total_V}× Verdadeiro  /  {total_F}× Falso"

    print(f"\n  Classificação : {classe}")
    print("═" * 62)
