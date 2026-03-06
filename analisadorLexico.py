# Módulo 1: Tokenizador (Análise Léxica)
# Responsável por quebrar a string de entrada em tokens reconhecíveis.

import re

# Tabela de tokens: (NOME, padrão regex)
TOKENS = [
    ('BICONDICIONAL', r'<->|↔'),
    ('IMPLICACAO',    r'->|→'),
    ('NAO',           r'~|¬|!'),
    ('E',             r'&&?|∧'),
    ('OU',            r'\|\|?|∨'),
    ('ABRE',          r'\('),
    ('FECHA',         r'\)'),
    ('VAR',           r'[a-zA-Z][a-zA-Z0-9]*'),
    ('ESPACO',        r'\s+'),
]

# Compila todos os padrões em uma única expressão regular
TOKEN_RE = re.compile('|'.join(f'(?P<{nome}>{padrao})' for nome, padrao in TOKENS))

# Dicionário para exibir o símbolo formal de cada conectivo
SIMBOLO_FORMAL = {
    'BICONDICIONAL': '↔',
    'IMPLICACAO':    '→',
    'NAO':           '¬',
    'E':             '∧',
    'OU':            '∨',
}

"""
    Tokenizar: recebe uma string com a fórmula lógica.
    Retorna uma lista de tuplas (TIPO, valor).
    Lança SyntaxError se encontrar símbolo inválido.
"""

def tokenizar(formula: str) -> list:
    
    resultado = []

    for match in TOKEN_RE.finditer(formula):
        tipo = match.lastgroup
        valor = match.group()

        if tipo == 'ESPACO':
            continue  # ignora espaços em branco

        if tipo is None:
            raise SyntaxError(
                f"\n  ERRO: Símbolo não reconhecido → '{valor}'\n"
                f"  Use apenas: variáveis (p, q, r...), ~, &, |, ->, <->, ( )"
            )

        resultado.append((tipo, valor))

    if not resultado:
        raise ValueError("  ERRO: Entrada vazia. Digite uma expressão lógica.")

    return resultado
