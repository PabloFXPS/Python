#Crie a classe Produto, onde podemos cadastrar nome e o preço.
#Crie também um método que mostre uma etiqueta de preço do produto.

from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        etiqueta = Panel(f"Produto: [blue]{self.nome}[/blue]\nValor: [red]R${self.valor:,.2f}[/red]",title="Etiqueta",width=23)
        return etiqueta

p1 = Produto("Notebook", 5000)
print(p1.etiqueta())

p2 = Produto("RTX2080", 2800)
print(p2.etiqueta())