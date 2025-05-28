# Exercício 84 - Lista composta e análise de dados
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.
'''cadastro = []
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
        print (v[0], end=" ")'''

# Exercício 85 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
'''valores = [[],[]]
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
print(f"\nPares {valores[0]}.\nImpares {valores[1]}.")'''

# Exercício 86 - Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
'''matriz = [[0,0,0],[0,0,0],[0,0,0]]
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
#     print()'''

# Exercício 87 - Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.