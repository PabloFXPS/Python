def separar():
    print("-="*20)
    print()
    

# Exercício Python 096:
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(largura,comprimento):
    separar()
    total = largura*comprimento
    print(f"A area de um terreno com {largura}x{comprimento} é de {total}m².")

largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura,comprimento)

# Exercício Python 097:
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    cont = len(msg)+1
    print("-" * cont)
    print(msg)
    print("-"* cont)


escreva("Os - a companham o tamanha dessa mensagem.")

# Exercício Python 098:
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo, e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(i,f,p):
    if p < 0:
        p *= 1
    if p == 0:
        p = 1
    print(f"Contagem de {i} até {f} de {p} em {p}:")
    from time import sleep
    sleep(1.5)
    if i < f: 
        cont = i
        while cont <= f:
            print(f"{cont} ",end="",flush=True)
            sleep(0.5)
            cont += p
        print("Fim.")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ",end="",flush=True)
            sleep(0.5)
            cont-=p
        print("Fim.")
    separar()

contador(i=1,f=10,p=1)
contador(i=10,f=0,p=2)

print("Faça o seu agora: ")
contador(i=int(input("Qual vai ser o inicio: ")),
         f=int(input("Qual o final: ")),
         p=int(input("De quantos em quantos: ")))