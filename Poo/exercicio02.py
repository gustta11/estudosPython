class Carro:
    def __init__(self,nome = "",ano = 0):
        self.nome = nome
        self.ano = ano

    def mensagem(self):
        return f"O carro é {self.nome} e o ano é {self.ano}"


c1 = Carro("Palio", 2016)
print(c1.mensagem())