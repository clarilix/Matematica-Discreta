# Módulo 3: Avaliador Semântico
# Percorre a AST recursivamente e calcula o valor lógico (True/False).

def avaliar(no: tuple, env: dict) -> bool:
    """
    no  → nó da Árvore Sintática Abstrata
    env → dicionário {variável: True/False}
    """
    operador = no[0]

    # Caso base: variável proposicional
    if operador == 'VAR':
        return env[no[1]]

    # Negação (operador unário)
    if operador == '¬':
        return not avaliar(no[1], env)

    # Operadores binários: avalia os dois lados primeiro
    esq = avaliar(no[1], env)
    dir = avaliar(no[2], env)

    if operador == '∧':
        return esq and dir                  # conjunção

    if operador == '∨':
        return esq or dir                   # disjunção

    if operador == '→':
        return (not esq) or dir             # implicação: ¬p ∨ q

    if operador == '↔':
        return esq == dir                   # bicondicional: mesmos valores


def coletar_variaveis(no: tuple) -> set:
    """Percorre a AST e retorna o conjunto de variáveis encontradas."""
    if no[0] == 'VAR':
        return {no[1]}
    if no[0] == '¬':
        return coletar_variaveis(no[1])
    return coletar_variaveis(no[1]) | coletar_variaveis(no[2])


def coletar_conectivos(tokens: list) -> list:
    """Retorna os conectivos presentes na expressão (sem repetição)."""
    from analisadorLexico import SIMBOLO_FORMAL
    vistos = set()
    lista = []
    for tipo, _ in tokens:
        if tipo in SIMBOLO_FORMAL and tipo not in vistos:
            lista.append(SIMBOLO_FORMAL[tipo])
            vistos.add(tipo)
    return lista
