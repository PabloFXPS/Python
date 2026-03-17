# Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar
#e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
#Considere: Consumo padrão: 400g por pessoa e preço R$82,40/kg

from rich import print
from rich.panel import  Panel

class Churrasco:
    def __init__(self,quantidade):
        self.quantidade = quantidade
        self.preco = 82.40
        self.consumo = 0.4 #kg

    def comprar_carne(self):
        return self.quantidade * self.consumo
    def custo_total(self):
        return self.comprar_carne() * self.preco
    def preco_por_pessoa(self):
        return self.custo_total() / self.quantidade

    def analisar(self):
        tabela = Panel(f"[red]Total de carne Kg por pessoa: {self.comprar_carne():,.1f}kg[/red]\n[blue]Preço total: R${self.custo_total():,.2f}[/blue]\n"
                       f"Preço por pessoa: R${self.preco_por_pessoa():,.2f}",title=f"Churrasco para {self.quantidade} pessoas",width=40)
        return tabela

c1 = Churrasco(int(input("Quantos pessoas vão para o churrasco? ")))
print(c1.analisar())