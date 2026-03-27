#Crie a classe Caneta, que simule o funcionamento de uma caneta colorida, pode escrever frases ca cor relativa.
from rich import print

class Caneta:
    def __init__(self,cor:str,tampada:bool = True):
        self.tampada = tampada

        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case "amarelo":
                escolha = "[yellow]"
        self.cor = escolha

    def destampar(self):
        self.tampada = False

    def escrever(self,frase:str):
        if self.tampada:
            print(f"[red] !!Caneta ainda esta tampada!!")
        else:
            print(f"{self.cor}{frase}",end="")

c1 = Caneta("vermelha")
c1.destampar()
c1.escrever("Olá")

c2 = Caneta("verde")
c2.destampar()
c2.escrever(",")

c3 = Caneta("azul")
c3.destampar()
c3.escrever("Mundo")

c4 = Caneta("amarelo")
c4.destampar()
c4.escrever("!")