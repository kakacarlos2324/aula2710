class caneta:
    def __init__(self,cor):
        self.cor = cor
        self.dono = None

class pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.caneta = nome

    def pegar_caneta(self, nome, caneta):
        self.caneta = caneta
        self.nome = nome
        print(f"o {self.nome} pegou a caneta {caneta}")

pessoa1 = pessoa("carlos")
pessoa1.pegar_caneta("carlos" , "azul")