from random import randint


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(1000, 1999)
        return rand


# p1 = Pessoa('João', 24)
p1 = Pessoa.por_ano_nascimento('João', 1998)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(p1.gera_id())
