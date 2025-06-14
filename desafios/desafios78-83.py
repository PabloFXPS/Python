# Desafio 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
num = []
for c in range(0,5):
    num.append(int(input(f"Digite o {c+1}° numero: ")))
print("=-="*11)
print(f"Sua lista ficou: {num}\n")
print (f"O maior valor foi {max(num)} nas posições: ",end="")
for i,v in enumerate(num):
    if num[i] == max(num):
        print (i+1,end=" ")
print (f"\nO menor valor foi {min(num)} nas posições: ",end="")
for i,v in enumerate(num):
    if num[i] == min(num):
        print(i+1,end=" ")

# Desafio 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
listanum = list()
numeros = 0
print("Adicione valores diferente. Caso, o valor ja possua na lista ele nao será colocado.")
while True:
    numeros=(int(input("Numeros: ")))
    if numeros in listanum:
        print("Valor ja existente, Tente outro.")
    else:    
        listanum.append(numeros)
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar [s/n] ?: ")).strip().upper()[0]
    if resposta == "N":
        break
print("-=-"*12)
listanum.sort()
print(f"Os valores digitados foram: {listanum}")

# Desafio 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
listnum = []
num = 0

for cont in range (0,5): 
    num = int(input(f"Digite o {cont+1}° numero: "))
    if cont == 0 or num > listnum[-1]:
        listnum.append(num)
    else:
        posição = 0
        while posição < len(listnum):
            if num <= listnum[posição]:
                listnum.insert(posição,num)
                break
            posição +=1       
print("-="*12)
print(f"A sequencia em ordem fica: {listnum}")

# Desafio 81: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input("Digite um numero: ")))
    reposta =" "
    while reposta not in "SN":
        reposta= str(input("Quer continuar [S/N] ? R:")).strip().upper()[0]
    if reposta == "N":
        break 
print(f"A quantidade de numeros digitados foram {len(lista)}.")
lista.sort(reverse=True)
print(f"A lista em ordem decresente: {lista}")
if 5 in lista:
    print ("O valor 5 foi digitado na lista.")
else:
    print("O valor 5 nao foi digitado.")

# Desafio 82: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

par =[]
impar =[]
listanum = []
while True:
    listanum.append(int(input("Digite um numero: ")))
    reposta = " "
    while reposta not in "SN":
        reposta = str(input("Quer continuar[S/N]. R: ")).strip().upper()[0]
    if reposta == "N":
        break
print("-="*13)
print(f"A sua lista ficou os numeros: {listanum}")
for c,valor in enumerate(listanum):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f"Os valores {par} são pares.\nOs valores {impar} são impares.")

# Desafio 83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expres = []
ex = str(input("Digite sua expressão ex (a+b): "))
for x in ex:
    if x == "(":
        expres.append("(")
    elif x == ")":
        expres.remove("(")
if "(" in expres:
    print("Expressão invalida.")
else:
    print ("Expressão valida.")