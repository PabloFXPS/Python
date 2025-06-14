# Exercício 90 - Cadastro de um Aluno
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input("Qual o nome do aluno ? R: "))
aluno['Nota 1'] = float(input("Qual a primeira nota ? R: "))
aluno["Nota 2"] = float(input("Qual a segunda nota ? R: "))
media = (aluno["Nota 1"]+aluno["Nota 2"]) / 2
print("-="*15)
for i,v in aluno.items():
    print(f"O {i} é igual a {v}.")
print(f"Sua média é {media}.")
if 6 <= media < 11:
    print("Aprovado.")
elif 0 <= media <6:
    print ("Recuperação.")
else:
    print("Dados incorretos.")

# Exercício 91 - Jogo de Dados em Python
# # Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
