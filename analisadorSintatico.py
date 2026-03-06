# Módulo 2: Analisador Sintático (Parser LL(1))
# Constrói uma Árvore Sintática Abstrata (AST) a partir dos tokens.
#
# Gramática com precedência (menor → maior prioridade):
#   ↔  <  →  <  ∨  <  ∧  <  ¬  <  átomo / ( )

class analisadorSintatico:

    def __init__(self, tokens: list):
        self.tokens = tokens
        self.pos = 0  # posição atual na lista de tokens

    def _peek(self):
        """Olha o token atual sem consumir."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None  # fim da lista

    def _consumir(self, tipo_esperado=None):
        """Consome e retorna o token atual. Valida o tipo se fornecido."""
        if self.pos >= len(self.tokens):
            raise SyntaxError("  ERRO: Expressão incompleta — token esperado ao final.")

        token = self.tokens[self.pos]

        if tipo_esperado and token[0] != tipo_esperado:
            raise SyntaxError(
                f"  ERRO: Esperado '{tipo_esperado}', mas encontrei '{token[1]}'."
            )

        self.pos += 1
        return token

    # ── Ponto de entrada ─────────────────────────────────────
    def parse(self):
        """Inicia o parse e verifica se toda a entrada foi consumida."""
        arvore = self._bicond()

        if self._peek() is not None:
            raise SyntaxError(
                f"  ERRO: Token inesperado → '{self._peek()[1]}'"
            )

        return arvore

    # ── Regras da gramática (ordem = precedência crescente) ──

    def _bicond(self):
        """↔  — menor precedência"""
        esq = self._impl()
        while self._peek() and self._peek()[0] == 'BICONDICIONAL':
            self._consumir()
            dir = self._impl()
            esq = ('↔', esq, dir)
        return esq

    def _impl(self):
        """→"""
        esq = self._ou()
        while self._peek() and self._peek()[0] == 'IMPLICACAO':
            self._consumir()
            dir = self._ou()
            esq = ('→', esq, dir)
        return esq

    def _ou(self):
        """∨"""
        esq = self._e()
        while self._peek() and self._peek()[0] == 'OU':
            self._consumir()
            dir = self._e()
            esq = ('∨', esq, dir)
        return esq

    def _e(self):
        """∧"""
        esq = self._nao()
        while self._peek() and self._peek()[0] == 'E':
            self._consumir()
            dir = self._nao()
            esq = ('∧', esq, dir)
        return esq

    def _nao(self):
        """¬  — maior precedência entre conectivos"""
        if self._peek() and self._peek()[0] == 'NAO':
            self._consumir()
            return ('¬', self._nao())  # recursivo: ~~p funciona
        return self._primario()

    def _primario(self):
        """Variável ou subexpressão entre parênteses"""
        token = self._peek()

        if token is None:
            raise SyntaxError("  ERRO: Expressão incompleta.")

        if token[0] == 'VAR':
            self._consumir()
            return ('VAR', token[1])

        if token[0] == 'ABRE':
            self._consumir()           # consome '('
            no = self._bicond()        # avalia o interior
            self._consumir('FECHA')    # consome ')'
            return no

        raise SyntaxError(
            f"  ERRO: Token inesperado → '{token[1]}'. Esperava variável ou '('."
        )
