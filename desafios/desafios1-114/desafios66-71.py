#66 crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai para quando o usuario digitar o valor 999, que é a condição de parada. No final mostre a quantidade de numeros digitados e a soma deles (desconsiderando o 999).
soma = cont = 0
while True:
    num = int(input("Digite um numero [para encerrar digite 999]: "))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print (f"Quantidade de numeros: {cont}.\nSoma de todos : {soma}.")

#67 faça um programa que mostre a tabua de varios numeros, um de cada vez para cada valor digitado pelo usuario. O programa sera interrompido quando o numero for negativo.
cont = 0 
while True:
    num = int(input("De qual numero vc deseja ver a tabuada. Digite um numero negativo para encerrar: "))
    if num > 0:
        print ("="*20)
        for cont in range(11):
            print(f"{num} X {cont} = {num*cont}", end="\n")
        print("="*20)
    else:
        print("Fim")
        break

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

# 69 crie um programa que leia a idade e sexo de cada pessoa. No final mostre se quer ou nao continuar e
# a)quantas pessoas tem +18
# b)quantos homens foram cadastrado
# c)quantas mulheres com -20
cont = 1
maior = homens = mulheres = 0
while True:
    print("=-="*7,f"\nCadatre a {cont}° pessoa")
    print("=-="*7)
    sex = " "
    while sex not in "MF":
        sex = str(input("Qual o sexo ? [M/F]\nReposta: ")).strip()[0].upper()
    idade = int(input("Qual a idade ?\nResposta: "))
    if idade >= 18:
        maior += 1
    if sex == "M":
        homens += 1
    if sex == "F" and idade < 20:
        mulheres += 1
    escolha = " "
    while escolha not in "SN":
        print("=-="*7)
        escolha = str(input("Quer continuar [S/N]? ")).strip()[0].upper()
        print("=-="*7)
    cont +=1
    if escolha == "N":
        break
print (f"\nDos cadastros fornecidos:\nQuantos são maiores de 18: {maior}.\nQuando Homens foram cadastrado: {homens}.\nQuantas mulheres menores de 20: {mulheres}.")

# 70 crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuario vai continuar e no final, mostre:
# a)qual é o total gasto na compra x
# b)quantos produtos custam mais de 1000 x
# c)qual o nome do produto mais barato


barato = ""
cont=caro = menor= total = 0
print("=-="*7,end="\nLista de compra\n")
print("=+="*7)
while True:
    print("=-="*7,end=f"\n{cont+1}° Produto\n")
    produto = str(input("nome do produto: "))
    preço = float(input("Preço: R$"))
    total += preço
    cont +=1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    escolha = " "
    if preço > 1000:
        caro += 1
    while escolha not in "SN":
        escolha = str(input("Quer continuar [S/N]: ")).strip()[0].upper()
    if escolha == "N":
        break
print(f"O total dos {cont} produtos é : R${total}\nQuantidade dos produtos acima de R$1000 = {caro}.\nProduto mais barato: {barato}")


#71 crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual sera o valor a ser sacado(Int) e o programa vai informar quantos cedulas de cada valor serão entregues.
#considere que o caixa possui cedulas de 50, 20, 10 e 1
c=v=d=u= 0
cinq=50
total = int
valor = int(input("Qual o valor que você quer sacar ?\nColoque apenas numeros inteiros\nSaque: R$"))
total = valor
while True:
    while total >0:
        if total>=50:
            total -= cinq
            c +=1
        elif total >= 20 and total < 50:
            total -=20
            v+=1
        elif total >= 10 and total < 20:
            total -=10
            d +=1
        elif total <10 and total >0:
            total -=1
            u+=1 
    break
print (f"Notas de cinqunta: {c}" if c > 0 else "")
print(f"Notas de vinte: {v}"if v >0 else"")
print(f"Notas de Dez: {d}" if d>0 else "")
print (f"Notas de um:{u}"if u>0 else "")