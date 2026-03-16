#Crie a classe Funcionário, onde podemos cadastrar o nome,setor e cargo.
#Crie também um método que permita ao funcionário se apresentar.
from rich import print
from rich import inspect

class Funcionario:
    #Atributos geral
    empresa = "UBER"
    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f"Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor {self.setor} da empresa {Funcionario.empresa}."

c1 = Funcionario("Pedro","TI","Programador")
print(c1.apresentacao())

c2 = Funcionario("Maria","Administração","Diretora")
print(c2.apresentacao())