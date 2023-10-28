class endereco():
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

class pessoa():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        print(f"pessoa {nome} mora em endereco{endereco}")
endereco1 = endereco("avenida minha 23,5", " são joão ")
pessoa1 = pessoa(nome="carlos", endereco = endereco1.cidade )
