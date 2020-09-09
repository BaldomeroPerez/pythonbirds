class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):  # depois de virgula entrou none que estava em baixo
        self.idade = idade
        self.nome = nome  #nome entro no lugar de None
        self.filhos=list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'


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
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)  #atributo de instancia (__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(),luciano.nome_e_atributo_de_classe())
