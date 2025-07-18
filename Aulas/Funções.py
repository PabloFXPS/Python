from encodings.rot_13 import rot13


def separar(): #Exemplo de uma função. Algo que vai precisar fazer várias vezes.
    print("-="*20)
separar() #Não precisa colocar print, só chamar a função com () no final.

print("Curso")
separar()
print("python")
separar()

#Para mensagens que se repetem, mas com modificações. MSG é um parametro que a função
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
#para criar uma função que vai receber vários tipos de números, use *num *<se refere ao desempacotar.
def contador(*num):
    tam = len(num)
    print(f"Os valores enviados foram {num} com o total de {tam} números.")

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2) 
#os valores viram uma tupla, então os comandos com tuplas funcionam.

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
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#-=-Interact HELP-=-

#Se usa para ver como um comando ou biblioteca funciona. Da para acessar no console digitando help().
#2 outras formas:
help(input) #<e coloque o comando que você quer ver.

print(print.__doc__)

#-=-Docstrings-=-

#É um manual de como a função que você criou funciona EX:
def contador(i,f,p):
    """ Função contador:
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    Função criada por Curso em Video.
    """
    c=i
    while c<=f:
        print(c,end=" ")
        c+=p
    print("Fim")
contador(1,10,1)
help(contador)

#-=-Parâmetros Opcionais=-=

#Para fazer uma def com partes opcionais 1 ou todos os parâmetros reais devem receber 0.
def somar(a=0,b=0,c=0):#←Parâmetros Reais.
    x= a+b+c
    print(f"A soma de {a}+{b}+{c} é = {x}.")
#Ex de parâmetros formais:
somar(1,2,3)
somar(2,5)
somar(1)
somar()

#-=-=Escopo de Variáveis-=-=

#São divididos em 2: Global e local
def teste():
    #global n <- Evita de criar outra variável N e usa a global. Então o N vai receber 2.

    x = 8 #<- Local: Só tem valor tendo da Função.
    n=4 #Se eu criar outro N nele tem valor aqui e vai ter 2 variáveis com o mesmo nome, mas com valores diferentes.
    print(f"N dentro vale {n}.")
    print(x)

n=2 #<- Global: Ela tem alcance em todo o código.
teste()
print(f"N fora vale {n}.")

#print(X) <- vai dar erro por que aqui ela não tem valor.

#-=-Retornando Valores-=-

#Return faz que os parâmetros formais recebam resultados individuais.
def somar2(a=0,b=0,c=0):
    x=a+b+c
    return x

r1=somar2(3,2,4)
r2=somar2(4,3)
r3=somar2(8)
print(f"A soma dos números {r1},{r2} e {r3}")