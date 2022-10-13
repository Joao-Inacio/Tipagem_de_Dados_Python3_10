class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'{self.nome} está falando...')


class Cliente(Pessoa):  # Herança
    def comprar(self):
        print(f'{self.nome} comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} estudando...')


c1 = Cliente('João', 23)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 25)
print(a1.nome)
a1.falar()
a1.estudar()
