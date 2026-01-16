#Declação de Classe
#=========================================================
class Gafanhoto:
    def __init__(self):
        #Atributo de Instância
        self.nome = ""
        self.idade = 0
                                    #Basicamente seria uma forma de um bolo, sem ingredientes.
    #Metodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos"
#=========================================================
#Declação de objetos
g1 = Gafanhoto()   #Instancia/cria a class. Faz g1 receber nome, idade. // Se executar sem colocar dados ele deixa nome "" e idade 0.

g1.nome = "Maria" #Metodos // ingredientes.
g1.idade = 18
print(g1.mensagem())
g1.aniversario() #Metodo -> ()
print(g1.mensagem(),"\n")

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 20
print(g2.mensagem())
