class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Sou Eu!'


if __name__ == '__main__':
    hugo = Pessoa(nome='Hugo_Leonardo')
    luciano = Pessoa(hugo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))  # Não é usual
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'eu'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(hugo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(hugo.olhos)
    print(luciano.olhos)
