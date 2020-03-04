class Pessoa:

    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Sou Eu!'


if __name__ == '__main__':
    p = Pessoa('Hugo_Leonardo')
    print(Pessoa.cumprimentar(p))  # Não é usual
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Hugo Gomes'
    print(p.nome)
    print(p.idade)