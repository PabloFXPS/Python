#57 faça um programa que leia o sexo de uma pessoa, mas só aceita os valores'M'ou'F'. Se errado peça para digitar dnv.
'''sx= str(input("Qual o seu sexo [M/F]: ")).strip().upper()[0]#upper[0] só pega a primeira letra.

while sx not in'MmFf':
    sx = str(input("Dados incorreto. Tente novamente: ")).strip().upper()[0]
print(f"O sexo informado foi {sx}")'''

#58 refazer o desafio 28. só que agora o loop vai até ele acertar.
#28 escreva um programa que faça o computador escolher um numero de 0 a 5 e paça para o usuario tentar descobrir qual foi o numero escolhido. O programa deverá escrever na tela se o usuario venceu ou perdeu

'''from random import randint

computador = randint(0,10)
tentativas = 1
print(" "*5,"Adivinhe o numero que estou pensando..."," "*5,"Dica: Esta entre 0 e 10.")
respostas = int(input("\nResposta: "))

while respostas != computador:
    if respostas > computador:
        respostas=int(input("Menos... Tente novamente: "))
    elif respostas < computador:
        respostas=int(input("Mais... Tente novamente: "))
    tentativas += 1
print(f"\nParabens você acertou !! \nTentativas: {tentativas}\nNumero do computador: {computador}")'''

# 59 crie um programa que leia o valores e no menu mostre 
# [1]Somar
# [2]Multiplicar
# [3]maior
# [4]novos numeros
# [5]Sair do programa

# reposta = 0
# num1 = float(input("Selecione o 1° numero: "))
# num2 = float(input("Selecione o 2° numero: "))

# while reposta != 5:
#     reposta = int(input('''Selecione umas das opções: 
#     [1]Somar
#     [2]Multiplicar
#     [3]Maior
#     [4]Novos numeros
#     [5]Sair do programa
# Resposta: '''))
#     if reposta == 1:
#         print (f"Resultado:{num1}+{num2}={num1+num2}.")
#     elif reposta == 2:
#         print (f"Resultado:{num1}x{num2}={num1 * num2}.")
#     elif reposta ==3:
#         if num1 > num2:
#             print (f"O numero {num1} é maior que {num2}.")
#         elif num1 == num2:
#             print(f"Os dois numeros são iguais.")
#         else:
#             print(f"O numero {num2} é maior que {num1}.")
#     elif reposta == 4:
#         num1 = float(input("1°-novo numero: "))
#         num2 = float(input("2°-novo numero: "))
#     elif reposta <1 or reposta > 5:
#         print("SELEÇÃO INCORRETA")
#     print("=-="*8) 
    
#60 leia o numero e faz o fatorial. Ex 5!=5X4X3X2X1=120

'''num = int(input("Digite um numero para calcular seu Fatorial: "))
cont = num
ftr = 1
print (f'Calculando {num}! = ',end='')
while cont > 0:
    print (f'{cont}', end='')
    print (" X " if cont > 1 else ' = ',end='')
    ftr *= cont
    cont -= 1
print(f'{ftr}')'''

#61 Refaça o desafio 51. lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos.
'''print ("Progressão aritmetica")
pm = int(input("Qual é o primeiro termo: "))
rz = int(input ("Qual é a razão: "))
qtt = int(input("Qual a quantidade de termos que você quer ver: "))
cont = 0
print("Resultado é:",end=" ")
while cont != qtt:
    termos = pm + cont *rz
    cont += 1
    print (f"{termos} ", end="")'''

#62 melhore o 61. só que agora ele vai poder mostrar mais X termos, encerra quando o usuario digita 0 nos termos.
'''print ("Progressão aritmetica 2.0")
pm = int (input("Qual é o primeiro termo: "))
rz = int (input("Qual a razao: "))
qtt = int(input("Quantos termos você quer ver: "))
termo = pm
mais = qtt
total = 0
print(f"{pm}: ",end="")
while mais != 0: 
    cont = 0
    while cont < mais:
        termo += rz
        print (f"{termo}", end="-"if cont < mais - 1 else "")
        cont +=1
        total +=1
    mais = int(input("\nQuer ver mais quantos termo ? 0 Para encerrar.\nResposta:"))
print(f"\nEncerrado. A quantidade de termos mostrado foi: {total}")'''

#63 escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma seguencia de fibonacci.
'''print (5*"=","Sequencia de Fibonacci","="*5)

termos=int(input("\nQuantos termos você quer ver: "))
cont = 1
t1 = 1
t2 = 1
print(f"{t1}-{t2}",end="-")
while cont != termos:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f"{t3}",end="-")
    cont +=1
print("Fim")'''
#Mostrar mais termos.
'''print (5*"=","Sequencia de Fibonacci","="*5)

termos=int(input("\nQuantos termos você quer ver: "))
cont = 0
t1 = 1
t2 = 1
mais = termos
print(f"{t1}-{t2}",end="-")
while mais !=0:
    cont = 1
    while cont <= mais:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print(f"{t3}",end="-"if cont <= mais-1 else"-Pausa")
        cont +=1
    mais = int(input("\nQuer ver mais termos ? 0 para sair.\nResposta: "))
print("Encerrado.")'''


#64 crie um programa que leia varios numeros inteiros, mostre quantos numeros foram digitados e qual foi a soma entre eles. Encerra quando digita 999.
'''num = total = cont = 0
print("Ao digitar um numero ele somará com o anterior. Para encerrar digite 999")
while num != 999:
        num = int(input("Numero: "))
        if num != 999:
            total += num
            cont += 1
print(f"A soma dos {cont} digitados foi = {total}")'''

#65 crie um programa que leia varios numeros inteiros, mostre a media, maior e menor. O programa pergunte se ele quer ou nao parar.
'''print("Ao digitar um numero e no final o programa mostrara a media, o maior numero e o menor.")
cont = media = num = total = maior = menor = 0
resposta = ""
lista = []
while resposta != "n":
    num = int(input("Digite um numero: "))
    resposta = str(input("Quer continua? [s/n]: ")).lower().strip()[0]
    if resposta not in 'sn' or num == str:
        print("Dados incorreto")
        break
    lista.append(num)
    cont +=1
    total += num
    if resposta == "n" and cont == 1:
        print (f"Você só digitou um numero: {lista}") 
media = total / cont
if cont >= 2 :print (f"Os numeros digitados foram:{lista}\nMenor numero: {min(lista)}\nMaior numero: {max(lista)}\nMedia: {media}")'''
