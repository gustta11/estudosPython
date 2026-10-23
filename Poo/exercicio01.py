class Carro:
    def __init__(self):
        self.nome = ''
        self.ano = 0

    def mensagem(self):
        return f"O carro é {self.nome} e o ano é {self.ano}"


c1 = Carro()
c1.nome = "Palio"
c1.ano = 2016
print(c1.mensagem())

