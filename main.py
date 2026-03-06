
from tabela import exibir_tabela

# ──────────────────────────────────────────────────
#  FORMATO DE ENTRADA ACEITO:
#
#  Variáveis    →  p, q, r, p1, q2  (letras/números)
#  Negação      →  ~p   ou  ¬p
#  Conjunção    →  p & q  ou  p ∧ q
#  Disjunção    →  p | q  ou  p ∨ q
#  Implicação   →  p -> q  ou  p → q
#  Bicondicional→  p <-> q  ou  p ↔ q
#  Parênteses   →  (p & q) -> r
# ──────────────────────────────────────────────────

def menu():
    print("\n" + "═" * 62)
    print("  BEM-VINDO AO ANALISADOR DE LÓGICA PROPOSICIONAL")
    print("═" * 62)
    print("  Digite uma expressão lógica para gerar a Tabela-Verdade.")
    print("  Digite 'sair' para encerrar.")
    print("  Digite 'exemplos' para ver exemplos de entrada.")
    print("─" * 62)

def mostrar_exemplos():
    exemplos = [
        "p -> q",
        "~p | q",
        "p & q",
        "(p & q) -> p",
        "p | ~p",
        "p & ~p",
        "(p -> q) <-> (~q -> ~p)",
        "(p | q) -> r",
    ]
    print("\n  Exemplos de expressões válidas:")
    for i, ex in enumerate(exemplos, 1):
        print(f"    {i}. {ex}")


# Execução do programa
if __name__ == "__main__":
    menu()

    while True:
        entrada = input("\n  Digite a expressão: ").strip()

        if entrada.lower() == 'sair':
            print("\n  Encerrando. Até logo!\n")
            break

        if entrada.lower() == 'exemplos':
            mostrar_exemplos()
            continue

        if not entrada:
            print("  Entrada vazia. Tente novamente.")
            continue

        try:
            exibir_tabela(entrada)
        except (SyntaxError, ValueError) as erro:
            print(f"\n  {erro}")
            print("  Verifique a expressão e tente novamente.")
 