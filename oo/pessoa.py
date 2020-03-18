class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Sou Eu!'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    hugo = Homem(nome='Hugo_Leonardo')
    luciano = Homem(hugo, nome='Luciano')
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
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), luciano.nome_e_atributos_de_classes())
    pessoa = Pessoa('anonino')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(hugo, Pessoa))
    print(isinstance(luciano, Homem))
