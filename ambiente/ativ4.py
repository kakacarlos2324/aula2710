class Cabeça:
    def __init__(self, expressao):
        self.expressao = expressao

class Boneco:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura
        self.cabeça = Cabeça("neutra")

    def destruir(self):
        self.cabeça = None

# Exemplo de uso:
boneco1 = Boneco("Boneco 1", 30)

# Acessando a expressão da cabeça do boneco
print(boneco1.cabeça.expressao)  # Saída: neutra

# Destruindo o boneco
boneco1.destruir()
# Agora, a cabeça do boneco1 também foi destruída

# Tentando acessar a expressão da cabeça após destruir o boneco
# Isso gerará