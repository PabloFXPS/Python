class ContaBancaria:
    """
    cria uma conta bancaria que permite fazer saques e depósito.
    """
    def __init__(self,id,nome,saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} do titular {self.titular} tem R${self.saldo:,.2f} reais"

    def depositar(self,valor):
        self.saldo += valor
        print(f"Deposito de valor R${valor:,.2f} autorizado na conta  de id:{self.id}")

    def sacar(self,valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R${valor:,.2f} na conta {self.id}: Saldo INSUFICIENTE.")
        else:
            self.saldo -= valor
            print(f"saque de R${valor:,.2f} autorizado na conta de id:{self.id}")

c1 = ContaBancaria(10,"pablo", 2000)
c1.depositar(100)
c1.sacar(5000)

print (c1)