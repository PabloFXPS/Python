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

#==================================================================================================================
class Pessoa:
    """
    Essa classe cria uma pessoa, que tenha nome e idade.
    """
    def __init__(self,n = "",i = 0):
        self.nome = n
        self.idade = i

    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos"

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"

p1 = Pessoa(n="maria",i=17) #Metodo indicado
p1.aniversario()
print(p1.mensagem())

print(p1.__doc__)
print(p1) #Caso deixe só p1 o método __str__ retorna a mensagem que voce colocar la
print(p1.__dict__)        #atributo: Retornam como dicionário
print(p1.__getstate__())  #metodo: mesma coisa
print(p1.__class__) #mostra a qual classa p1 pertence