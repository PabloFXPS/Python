#28 escreva um programa que faça o computador escolher um numero de 0 a 5 e paça para o usuario tentar descobrir qual foi o numero escolhido. O programa deverá escrever na tela se o usuario venceu ou perdeu

'''from random import randint

pc = randint(0,5) #randomiza numeros de 0 a 5
print ("=-=" * 20)
print ("Tente adivinhar o numero que o computador escolheu de 0 a 5")
print ("=-=" * 20)

jogador = int(input("escolha seu numero: "))

#Caso o usuario digite um numero > 5
if  jogador <0 or jogador > 5:
    print ("Você digitou um numero maior que 5 ou menor que 0. Perdeu.")
else:
    if jogador == pc:
        print ("\nResultado: Você acertou.")
    else:
        print ("\nResultado:Errou!!! \nSeu numero:{} \nNumero do computador:{}".format(jogador,pc))'''

#29 escreva um programa que leia a velocidade de um carro. Se ele utrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa custa R$7.00

'''velocidade = float(input("Qual é a sua velocidade ? "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print ("Você passou acima do limite da via. Sua multa vai ficar em {:.2f}". format(multa))
else:
    print("Pode continuar sua viagem. Cuidado para não ultrapassar o limite da via.")'''

#30 crie um programa que leia um numero inteiro e m/ostre se ele é impar ou par.

'''print("Vamos descobrir se o numero é impar ou par.\n!!Digite apenas numeros inteiros!!")
numero = int(input("Digite um numero: "))

resultado = numero % 2 

if resultado == 0:
        print("{} é par.".format(numero))
else:
        print("{} é impar.".format(numero))'''

#31 desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando R$0,5 por KM até 200KM e para viagens mais longas 0.45

'''print ("============RODOVIARIA============\nPara viagens de até 200Km serão cobrado R$0,5 por KMV. Viagens acima disso são R$0.45 por KM.")
distancia = float(input("Qual a distancia da sua viagem ? "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
#preco = disctancia * 0.50 distancia <= 200 else distancia * 0.45 | simplifica

print ("Sua passagem ficou no preço de R${:.2f}".format (preco))'''

#32 faça um programa que leia um ano qualquer e mostre se ele é bissexto.

'''from datetime import date

ano = int(input("Vamos ver se o seu ano é bissexto. Em que ano vc esta ? Coloque 0 para analisar o ano atual. "))
if ano ==0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 !=0) or ano % 400 == 0:
    print("{} é um ano bissexto".format(ano))
else:
    print("{} não é um ano bissexto.".format(ano))'''

#33 faça um programa que leia tres numeros e mostre qual é o maior e qual o menor.

'''print ("Digite 3 numeros. O progrma ira mostrar qual é o maior e qual o menor.")

n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))
n3 = float(input("digite o terceiro numero: "))
#menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#maior
maior = n1
if n2 > n3 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

print ("{:.1f} foi o maior.\n{} foi o menor numero".format(maior,menor))'''

#34 escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para superior a R$1.250,00 aumento de 10%. Para inferiores ou iguais é de 15%.

'''print ("===aumento de salario===\nPara salario de R$1.250,00 será 10% de aumento. Para inferior ou igual é de 15%")

salario = float(input("Qual é o seu salario ? \nR$:"))

if salario <= 1250:
    aumento = salario+(salario*(15/100))
else:
    aumento = salario+(salario*(10/100))

print ("\nanterior: R${:.2f}.\nCom aumento: R${:.2f}.".format(salario,aumento))'''

#35 desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo.

'''print ("Digite 3 lados para saber se é possivel fazer um triangulo.")
r1 = float(input("Digite o primeiro numero: "))
r2 = float(input("Digite o segundo numero: "))
r3 = float(input("Digite o terceiro numero: "))

if (r2-r3)<r1<(r1+r3) and (r1-r3)<r2<(r1+r3) and (r1-r2)<r3<(r1+r2):
    print ("\nCom os valores {},{} e {} da para fazer um triangulo.".format(r1,r2,r3))
else:
    print("\nNão é possivel fazer um triangulo com esses valores.")'''


