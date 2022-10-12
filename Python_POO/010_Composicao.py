class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))  # Composição

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')


cli1 = Cliente('Luiz', 32)
cli1.insere_endereco('Fortaleza', 'CE')
print(cli1.nome)
cli1.lista_enderecos()
print()

cli2 = Cliente('Maria', 25)
cli2.insere_endereco('Natal', 'RN')
cli2.insere_endereco('Salvador', 'BA')
print(cli2.nome)
cli2.lista_enderecos()
print()

cli3 = Cliente('João', 24)
cli3.insere_endereco('Mulungu', 'CE')
print(cli3.nome)
cli3.lista_enderecos()
print('#'*50)
