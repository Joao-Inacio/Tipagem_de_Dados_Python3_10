class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')


class ClienteVIP(Cliente):
    def falar(self):
        super().falar()
        print('Falando outra coisa')


class AlunoVIP(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)


c1 = Cliente('Luiz', 23)
c1.comprar()
print()

c2 = ClienteVIP('Ana', 20)
c2.falar()
print()

c3 = AlunoVIP('Luiz', 37)
print(f'{c3.nome} {c3.falar()}')
