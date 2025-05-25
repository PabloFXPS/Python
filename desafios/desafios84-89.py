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

# Exercício 85 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.