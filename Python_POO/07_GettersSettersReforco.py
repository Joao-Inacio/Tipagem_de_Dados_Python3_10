# SETTER = Configurar um valor (=)
# GETTER = Obter um valor (.)

class Pessoa:
    def __init__(self):
        self._nome = ''

    @property  # GETTER
    def nome(self):
        return self._nome

    @nome.setter  # SETTER
    def nome(self, valor):
        self._nome = valor


p1 = Pessoa()
p1._nome = 'João'
print(p1._nome)
print(p1.nome)
