#36 escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.O programa vai perguntar o valor da casa, salario e quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o empréstimo será negado.

resp = int(input("Seja bem-vindo ao EmprestimoRapido\nQual seria o motivo para o emprestimo?\n1-Casa\n2-Carro\n3-outros\n"))

if resp == 2 or resp ==3:
    print("No momento só estamos trablalhando com emprestimo de Casa.")
if resp == str or resp > 3 or resp < 1:
    print("Seleção invalida Tente novamente.")
else:
    casa=float(input("\nQual seria o valor da casa ? "))

    salario=float(input("\nQual o seu salario ? "))

    anos=int (input("\nEm quantos anos pretende pagar ? "))

    PrestM = casa /(anos * 12)
    Limite= salario*0.3
    
    if PrestM <= Limite:
        print("Emprestivo APROVADO. Nossos mande seus dados para ser feita a verificação de credênciais.")
    else:
        print("Emprestivo NEGADO.")


#37 escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão.
#1-binario 2-octal 3-hexadecimal

print("-----Sistema de converção de numeros-----\n")
num=int(input("Digite um numero inteiro: "))
if num == str or num == float:
    print("Apenas numeros inteiros são validos.")
op=int(input("1-Binario\n2-Octal\n3-Hexacimal\nOpção: "))
if op == str or op == float:
    print("Opção incorreta.")
elif op == 1:
    resp= bin(num)[2:]
    print ("Seu numero foi {}.\nNa base binario fica:{}".format(num,resp))
elif op == 2:
    resp = oct(num)[2:]
    print("Seu numero foi {}.\nNa base octal fica:{}".format(num,resp))
elif op == 3:
    resp = hex(num)[2:]
    print ("Seu numero foi{}.\nNa base hexadecimal fica:{}".format(num,resp))
print ("-"*41)


#38 escreva que leia dois numero inteiro e compare-os, mostrando na tela uma mensagem:- o primeiro valor é maior/-o segundo valor é maior/-não existe valor maior, os dois são iguais.
print("Escreva 2 numeros e o computador vai analisar qual é maior o menor ou se são iguais.\n")

n1=float(input("Primeiro numero: "))
n2=float(input("Segundo numero: "))

if n1 > n2:
    print ("O primeiro numero é maior que o segundo.")
elif n2 > n1:
    print ("O segundo numero é maior que o primeiro.")
elif n1 == n2:
    print("Os 2 numeros são iguais.")

# 39 faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# -se ele ainda vai se alistar ao serviço militar/- se é a hora de se alistar/- se ja passou do tempo.
# Seu programa deverá mostrar o tempo que falta ou que ja passou do prazo.

from datetime import date
print ("Progama de alistamento obrigatorio.")

nascimento = int(input("Em que ano você nasceu? Exemplo:2009\nResposta: "))
if nascimento == str or nascimento == float:
    print("Dados incorreto.")
ano = date.today().year
idade = ano - nascimento
if idade == 18:
    print("Ja esta na hora de se alistar.")
elif idade < 18:
    print("Ainda não esta na hora. Falta {} anos para se alistar.".format(18-idade))
elif idade > 18:
    atraso = int(input("Você ja fez o alistamento ?\n1-Sim\n2-Não\nResposta: "))
    if atraso == 1:
        print("Então esta tudo certo.")
    elif atraso == 2:
        print("Você esta {} atrasado. Procure se alistar o mais rapido possivel.".format(idade - 18))
    else:
        print("Opção incorreta.")


#40 crie um programa que leia duas notas de um aluno e calcule sua média. mostrando uma mensagem no final, de acordo com a media atingida:
#-abaixo de 5.0 REPROVADO/-entre 5.0 e 6.9 RECUPERAÇÃO/-7+ APROVADO.

print("Calcule sua media escolar!!")
nota1 = float(input("Nota do 1° semestre: "))
nota2= float(input("Nota do 2° semestre: "))
media = (nota1+nota2)/2

if media < 5.0:
    print("Sua media escolar é {}. Você esta reprovado.".format(media))
elif media == 5.0 and media < 6.9:
  print("Sua media é {}. Você esta de recuperação, estude bastante.")
elif media >= 7.0 and media <= 10:
    print("Sua média foi {}. Aproveita as ferias".format(media))
else: 
   print ("Dados inserido de forma incorreta.")

# 41 a confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# Até 9 anos: mirim/14 infantil/19 junior/20 senior/+master

from datetime import datetime, timedelta

dtatual= datetime.now()

print("-"*10,"Primeiro campeonato de natação","-"*10,"\nIdade minima: 9 anos\nCategorias: \nMirim 9 anos\nInfantil 14 anos\nJunior 19 anos\nSenior 20 anos ou mais\n")

atleta = input("insira sua data de nascimento para fazer a inscrição?\nFormatado dia/mes/ano\nSua data: ")
atleta = datetime.strptime(atleta,"%d/%m/%Y")

idade = dtatual.year - atleta.year

if ( atleta.month < dtatual.month or atleta.day < dtatual.day): #revisar
    idade = idade - 1 
#classificação
if (idade == 9):
    print (f"Como você tem {idade}, vai participar da categoria: Mirim.")
elif(idade > 9 and idade <=14 ):
    print (f"Como você tem {idade}, vai participar da categoria: Infantil.")
elif (idade > 14 and idade <=19):
    print (f"Como você tem {idade}, vai participar da categotia: junior.")
elif(idade == 20):
    print(f"Como você tem {idade}, vai participar da categoria: Senior.")
elif (idade > 20):
    print (f"Como você tem {idade}, vai participar da categoria: Master.")
elif (idade < 9):
    print("Você não tem a idade minima.")

# 42 refaça o desafio 35 dos triangulos acrescentando o recurso de mostrar o tipo de triangulo:
# Equilátero: Todos os lados iguais.
# Isosceles: dois lados iguais.
# escaleno: todos diferentes.


print ("Digite 3 lados para saber se é possivel fazer um triangulo e seus tipos.")
r1 = float(input("Digite o primeiro numero: "))
r2 = float(input("\nDigite o segundo numero: "))
r3 = float(input("\nDigite o terceiro numero: "))

if (r2-r3)<r1<(r1+r3) and (r1-r3)<r2<(r1+r3) and (r1-r2)<r3<(r1+r2):
    print ("\nCom os valores {},{} e {} da para fazer um triangulo.".format(r1,r2,r3))
    if r1 == r2 == r3:
        print ("Seu triangulo é: Equilátero")
    elif r1 == r2 or r3 == r1 or r2 == r3 :     #ou r1 != r2 != r3 != r1 print("escaleno")
        print("Seu triangulo é: Isosceles")
    else:
        print("Seu triangulo é: escaleno")
else:
    print("\nNão é possivel fazer um triangulo com esses valores.")


# 43 desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu imc e mostre seus status, de acordo com a tabela:
# - 18.5: abaixo do peso.
# - 18.5 a 25: peso ideal.
# - 25 a 30: sobrepeso.
# - 30 a 40: obesidade. 
# - acima de 40: obesidade mórbida.

print ("-_"*5,"Calculadora de IMC","_-"*5)

peso = float(input("Para começarmos informe seu peso e altura.\nPeso Kg: "))
altura = float(input("Altura: "))

imc = peso / (altura**2)

print ("\nSeu imc: {:.1f}".format(imc))
if imc < 18.5:
    print ("Indice: Abaixo do peso")
elif  18.5 == imc <= 25:
    print ("Indice: Peso ideal")
elif 25 > imc <= 30:
        print ("Indice: Sobrepeso")
elif  30 > imc <= 40:
         print ("Indice: obesidade")
elif imc > 40:
          print ("Indice: obesidade morbida") 


# 44 elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# -à vista dinheiro/cheque: 10% de desconto.
# -à vista no cartão: 5% de desconto.
# -em até 2x no cartão: preço normal.
# -3x ou mais no cartão: 20% de juros.

print("=-="*20)

valor = float(input("Insira o valor total das compras do cliente.\nR$: "))

pagamento = int(input("Selecione a forma de pagamento\n1-Dinheiro/cheque\n2-Cartao\nEscolha: "))

if pagamento < 1 or pagamento >= 3:
    print("Opção incorreta.")
elif pagamento == 1: #Dinheiro / cheque
     desconto = valor - ((10/100)*valor)
     print ("\nVocê recebeu um desconto de 10% na sua compra.\nO pagamento ficou R${} .".format(desconto))
elif pagamento == 2: #cartão
     cart = int(input("\n1-Debito\n2-Credito\nResultado: "))
     if cart == 1: #Desconto no debito
        desconto = valor - ((5/100)*valor)
        print("Você recebeu um desconto de 5% na sua compra.\nO pagamento ficou R$:{}.".format(desconto))
     elif cart == 2: #creditos / parcelas
            cred = int(input("\nQuantas vezes vai ser o parcelamento?\nParcelas: "))
            if cred == 1 or cred == 2:
                print (f"\nO produto ficou no valor de {valor}.\nParcelas de R$ {valor/cred}.")
            if cred >= 3:
                juros = valor + ((20/100)*valor)
                print(f"Com as taxas da maquina o valor foi para R$ {juros}.\nValor por parcela: R$ {juros/cred}.")
print("=-="*20)

#45 crie um programa que faça o computador jogar jokenpô com você.

from random import randint

comput = randint(1,3)

print("=-="*10,"Jokempô","=-="*10)

jogador = int(input("Tente vencer a maquina em um jogo. Escolha 1 das alternativas a abaixo:\n1-Pedra\n2-Papel\n3-Tesoura\nEscolha: "))

print(f"\nO computador escolheu: {comput}\nJogador: {jogador}")

if comput == jogador: #empate
    print("\nOs dois escolheram a mesma coisa. EMPATE!!")
elif jogador == 1 and comput == 3:
    print("\nVocê ganhou !!!")
elif jogador == 2 and comput == 1:
    print("\nVocê ganhou !!!")
elif jogador == 3 and comput ==1:
    print("\nVocê ganhou !!!")
else:
    print("\nVocê perdeu.")
print("=-="*23)

#outro modo

from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')
comput = randint (0,2)
print(''' Tente ganhar da maquina no JOKENPÔ !!!!
Suas opções:
[0]Pedra
[1]Papel
[2]Tesoura''')
jogador = int(input("Qual sua jogada: "))

if 0 < jogador > 2:
    print("Opção invalida")
else:
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print ("PÔ")
    sleep(1)

    print(f"\nVocê escolheu {itens[jogador]} e o computador {itens[comput]}. ")

    if jogador == comput:
        print("Empate!!")
    elif jogador == 0 and comput == 2:
        print("Você ganhou!!!") 
    elif jogador == 1 and comput == 0:
        print("Você ganhou!!!")
    elif  jogador == 2 and comput == 1:
        print("Você ganhou!!!")
    else:
        print("Você perdeu :(")