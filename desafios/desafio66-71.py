#66 crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai para quando o usuario digitar o valor 999, que é a condição de parada. No final mostre a quantidade de numeros digitados e a soma deles (desconsiderando o 999).
'''soma = cont = 0
while True:
    num = int(input("Digite um numero [para encerrar digite 999]: "))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print (f"Quantidade de numeros: {cont}.\nSoma de todos : {soma}.")'''

#67 faça um programa que mostre a tabua de varios numeros, um de cada vez para cada valor digitado pelo usuario. O programa sera interrompido quando o numero for negativo.
'''cont = 0 
while True:
    num = int(input("De qual numero vc deseja ver a tabuada. Digite um numero negativo para encerrar: "))
    if num > 0:
        print ("="*20)
        for cont in range(11):
            print(f"{num} X {cont} = {num*cont}", end="\n")
        print("="*20)
    else:
        print("Fim")
        break'''

#68 faça um programa que joguei par e impar. O jogo para quando o jogador perder e no final mostre sua seguencia de vitoria.
from random import randint
seq = 0
print("Tente ganhar da maquina no par ou impar\n")
while True:
    cp = randint(0,10)
    user= int(input("Escolha seu numero de 0 a 10: "))
    escolha = str(input("Você quer par ou impar ? [P/I]: ")).upper().strip()[0] #coloca a escolha para maiusculo, sepera e pega só a primeira letra
    if user > 10 or user < 0 or escolha not in "PI":
        print("\nEscolha incorreta.\n")
    else:
        soma = user + cp 
        resultado = soma % 2
        if escolha == "P" and resultado == 0:
            print(f"\nVocê escolheu {user} e o computador {cp} no total foi {soma} Par.\nVocê ganhou, vamos ver até onde vc vai XD\n")
            seq +=1
        elif escolha == "I" and resultado == 1:
            print(f"\nVocê escolheu {user} e o computador {cp} no total foi {soma} Impar.\nVocê ganhou, vamos ver até onde vc vai XD\n")
            seq +=1
        else:
            print(f"\nVocê perdeu.\nSua escolha {user} a do computador {cp} total de {soma}.")
            break
print(f"Sua sequencia de vitorias foi: {seq}")