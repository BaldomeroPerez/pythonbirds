class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):  # depois de virgula entrou none que estava em baixo
        self.idade = idade
        self.nome = nome  #nome entro no lugar de None
        self.filhos=list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ =='__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo,nome='Luciano') #luciano entrou no lugar  de None (em branco)
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filhos in luciano.filhos:
        print(filhos.nome)
    luciano.sobrenome="Ramalho"
    #print(luciano.sobrenome)
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)


