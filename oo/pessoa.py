class Pessoa:
    def __init__(self, nome=None, idade=35):  # depois de virgula entrou none que estava em baixo
        self.idade = idade
        self.nome = nome  #nome entro no lugar de None

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ =='__main__':
    p = Pessoa('Luciano') #luciano entrou no lugar  de None (em branco)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = "Miro"
    print(p.nome)
    print(p.idade)
