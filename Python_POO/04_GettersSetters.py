class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):  # função que realoca para a variável
        return self._nome

    @nome.setter
    def nome(self, valor):  # função que recebe e trata
        self._nome = valor.title()

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor


p1 = Produto('camiseta', 50)
p1.desconto(25)
print(p1.nome, p1.preco)

p2 = Produto('blusa azul', 'R$20')
p2.desconto(50)
print(p2.nome, p2.preco)
