# Exercício 84 - Lista composta e análise de dados
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.
cadastro = []
pessoas = []
while True:
    pessoas.append(str(input("Nome: ")))
    pessoas.append(float(input("Peso: ")))
    cadastro.append(pessoas[:])
    pessoas.clear()
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if resposta == "N":
        break
print(f"Quantidade de pessoas cadastradas: {len(cadastro)}.")
pesos = [p[1] for p in cadastro] 
ma = max(pesos)
mi = min(pesos)
print (f"O maior peso é {ma} e sendo as pessoas:",end=" ")
for i,v in enumerate(cadastro):
    if v[1] == ma:
        print (v[0],end=" ")
print (f"\nO menor peso é {mi} e sendo as pessoas:",end=" ")
for i,v in enumerate(cadastro):
    if v[1] == min(pesos):
        print (v[0], end=" ")

# Exercício 85 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
valores = [[],[]]
valor = 0
for cont in range(1,8):
    valor = int(input(f"Digite o {cont}° numero: "))
    if valor % 2==0: 
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print("-="*30)
valores[0].sort
valores[1].sort
print(f"\nPares {valores[0]}.\nImpares {valores[1]}.")

# Exercício 86 - Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite o valor da coluna [{l}] [{c}]: "))
print("-="*12)

#Meu resultado
for p in matriz[0]:
    print(f"[{p:^4}]",end=" ")
print("\n")
for v in matriz[1]:
    print (f"[{v:^4}]",end=" ")
print("\n")
for x in matriz[2]:
    print (f"[{x:4}]",end=" ")

# #Estilo do curso
# for l in range(0,3):
#     for c in range(0,3):
#         print(f"[{matriz[l][c]:^6}]",end="")
#     print()

# Exercício 87 - Aprimore o desafio anterior, mostrando no final:
par =[]
spar = soma = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite o numero da matriz {[l]}{[c]}. R: "))
        if matriz[l][c] %2 ==0:
            spar += matriz[l][c] 
            par.append(matriz[l][c])

print("-="*15)
for l in range (0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^8}]",end="")
    print()
print("-="*15)
# a) A soma de todos os valores pares digitados.
print(f"A soma dos numeros pares:{par} é: {spar}.")

# b) A soma dos valores da terceira coluna.
for x in range (0,3):
    soma += matriz[x][2]
print(f"A soma da 3° coluna é: {soma}.")

# c) O maior valor da segunda linha.
maior = max(matriz[1])
print(f"O maior valor da segunda linha é: {maior}.")

# Exercício 88 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
num = list(range(1, 61))
from random import sample
from time import sleep
jogos = int(input("Quantos jogos vc quer sortear ? R:"))
print("-"*35)
for x in range(jogos):
    jogo = sample(num, 6)
    jogo.sort(reverse=False)
    print(f"{x+1}° Jogo = {jogo}")
    sleep(1)

# Exercício 89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1= float(input("Nota 1: "))
    nota2= float(input("Nota 2: "))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp = " "
    while resp  not in "SN":
        resp = str(input("\nQuer continuar ? [S/N] R:")).strip().upper()[0]
        print()
    if resp == "N":
        break
print("-="*20)

for i,v in enumerate(ficha):
    print(f"N° {i} | Nome: {v[0]} | Media: {v[2]} | ")
print("--"*20)
while True:
    aluno = int(input("Insira o N° do aluno que você deseja ver as notas. Para sair coloque [999]. \nR: "))
    if aluno == 999:
        print("\nPrograma finalizado.")
        break
    elif aluno > len(ficha)-1:
        print(f"Valor incorreto. A lista de alunos vai até {len(ficha)-1}.")
    elif aluno <= len(ficha)-1:
        print("-+-"*10)
        print(f"Aluno:{ficha[aluno][0]} | Notas:{ficha[aluno][1]}")
        print("-=-"*10)