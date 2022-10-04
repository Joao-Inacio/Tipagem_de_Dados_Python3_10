# SETTER = Configurar um valor (=)
# GETTER = Obter um valor (.)

class Pessoa:
    def __init__(self):
        self.atributo = ''

    @property
    def nome(self):
        return self.atributo

    @nome.setter
    def nome(self, valor):
        self.atributo = valor


p1 = Pessoa()
p1.atributo = 'João'
print(p1.atributo)
print(p1.nome)
