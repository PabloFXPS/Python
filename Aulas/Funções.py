def separar(): #Exemplo de uma função. Algo que vai precisar fazer varias vezes.
    print("-="*20)
separar() #Não precisa colocar print, só chamar a função com () no final.

print("Curso")
separar()
print("python")
separar()

#Para mensagens que se repetem mas com modificações. MSG é um parametro que a função
def mensagem(msg): 
    separar()      #MENSAGEM vai receber logo a baixo. |
    print(msg)
    separar()
mensagem("sistema de alunos")                       
mensagem("sistema 2") #Repete os 2 na função.

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

# a = 4          a = 8           a = 1       \
# b = 5          b = 9           b = 2        \   Exemplo:
# s = a + b     s = a + b       s = a + b     /   precisa fazer essas 3 somas usando as funções.
# print(s)      print(s)        print(s)     /     

def soma (a,b):
    s = a + b
    print(f"Resultado da soma de {a} + {b} = {s} ")

soma(a=4,b=5)
soma(b=8,a=9) #da para alterar as orders dos valores.
soma(1,2)
#caso coloque soma(4) ou soma(3,4,2) < só 1 ou mais de 2 valores, o programa da erro por que faltou parametro ou tem dms.

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#para criar uma função que vai receber varios tipos de numeros, use *num *<se refere ao desempacotar.  
def contador(*num):
    tam = len(num)
    print(f"Os valores enviados foram {num} com o total de {tam} numeros.")

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2) 
#os valores viram uma tupla, entao os comandos com tuplas funcionam.

#Agora com lista:
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6,5,4,3,2,4]
print(valores)
dobra(valores)
print(valores)