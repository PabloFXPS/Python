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
print ("Progressão aritmetica")
pm = int(input("Qual é o primeiro termo: "))
rz = int(input ("Qual é a razão: "))
qtt = int(input("Qual a quantidade de termos que você quer ver: "))
cont = 0
print(f"Resultado é:",end=" ")
while cont != qtt:
    termos = pm + cont *rz
    cont += 1
    print (f"{termos} ", end="")