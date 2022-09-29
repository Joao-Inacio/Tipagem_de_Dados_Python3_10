class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer agora porquê esta falando')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar pois está com a boca cheia')
        else:
            print(f'{self.nome} estar falando sobre {assunto}!')
            self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False


p1 = Pessoa('João', 23)
p1.comer('Uva')
p1.comer('Uva')

p1.falar('Espaço')
p1.parar_comer()
p1.falar('Buraco Negro')
p1.parar_falar()
p1.comer('Uva')
p1.falar('Espaço')
p1.parar_comer()

