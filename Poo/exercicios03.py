class ContaBancaria:
    """
        Cria uma conta para fazer saques e depósitos
    """

    def __init__(self, numeroConta, titular = "", saldo =0):
        self.id =  numeroConta
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"{self.titular} tem a conta de número {self.id} com saldo {self.saldo:,.2f}"

    def deposito(self, valor):
        self.saldo+=valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


p1 = ContaBancaria(745842,"Gustavo",5000)
print(p1)
p1.deposito(2000)
print(p1)
p1.saque(10000)
print(p1)