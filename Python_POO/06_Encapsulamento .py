"""
    public
    protected: _
    private: __ (Cria outro atributo)
"""


class BaseDe_Dados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados  # retorna a variável privada dados

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDe_Dados()
# bd.inserir_clientes(1, 'Otávio')
# bd.inserir_clientes(2, 'Miranda')
# bd.inserir_clientes(3, 'Rose')
# bd.lista_clientes()
# print(bd.__dados)
# bd.apaga_cliente(3)
# bd.lista_clientes()
print(bd.__dados)
