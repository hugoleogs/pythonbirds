class Pessoa:
    def cumprimentar(self):
        return 'Sou Eu!'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p)) # Não é usual
    print(p.cumprimentar())
