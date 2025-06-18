# Exercício 90 - Cadastro de um Aluno
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

'''aluno = dict()
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
    print("Dados incorretos.")'''

# Exercício 91 - Jogo de Dados em Python
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
'''from time import sleep
from random import randint
from operator import itemgetter
jogadores = {'j1': randint(1,6),
'j2': randint(1,6),'j3': randint(1,6),'j4': randint(1,6)}

rank = dict()

for v,i in jogadores.items():
    print(f"O {v} tirou: {i}.")
    sleep(1)
print("-="*20)
print("Rank")
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for v,i in enumerate(rank):
    print(f"O {i[0]} ficou e em {v+1}° com o numero : {i[1]}.")
    sleep(1)'''

# Exercício 92 - Cadastro de Trabalhador em Python
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
cadastro = {}
cadastro['Nome'] = str(input("Nome: "))
date = int(input("Ano de nascimento: "))
cadastro['Anos'] = datetime.now().year - date
cadastro['CDT'] =  int(input("Numero da Carteira de trabalho. Caso, não tenha digite 0. R: "))
if cadastro['CDT'] == 0:
    print()
    for i,v in cadastro.items():
        print(f"{i}: {v}")
else:
    cadastro['Contratado'] = int(input("Ano de contratação: "))
    cadastro['Salario'] = float(input("Digite seu salario: ")) 
    cadastro['Aposentadoria'] = cadastro['Anos'] + ((cadastro['Contratado'] + 35) - datetime.now().year)
    print()
    for i,v in cadastro.items():
        print(f"{i}: {v}")