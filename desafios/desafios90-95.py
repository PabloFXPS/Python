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
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from time import sleep
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
    sleep(1)

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
    
# Exercício 93 - Cadastro de Jogador de Futebol
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
partidas = list()
jogador = dict()
jogador['Nome'] = str(input("Digite o Nome do jogador: "))
jogador['jogos'] = jogos = int(input("Quantos jogos ele jogou: "))
if jogos == 0:
    print(f"O {jogador['Nome']} não jogou nem um dos jogos.")
else:
    for x in range(jogos):
        partidas.append(int(input(f"Quandos gols na {x+1}°: ")))
    jogador['gols'] = partidas[:] 
    jogador['total'] = sum(partidas)
    print("-="*20)
    print(jogador)
    print("=-"*20)
    for i,v in jogador.items():
        print(f"O campo {i} tem o valor {v}.")
    print("=="*20)
    print(f"O jogador {jogador["Nome"]} jogou {jogos}.")
    for i,v in enumerate(jogador["gols"]) :
        print(f"Na partida {i} e fez {v} gols.")

#Exercício 94 - Unindo Dicionários e Listas
#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário, e todos os dicionários em uma lista.
#No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade do grupo
#C) Uma lista com todas as mulheres
#D) Uma lista de pessoas com idade acima da média
pessoas = dict()
cadastros = list()
contador = 0
tidade = 0

while True:
    pessoas.clear()
    print(f"Cadastro N° {contador+1}.\n")
    pessoas["Nome"] = str(input("Nome: "))
    pessoas["Masculidade"] = " "

    while pessoas["Masculidade"] not in "MF":
        pessoas["Masculidade"] = str(input("Masculidade [M/F]: ")).strip().upper()[0]
        if pessoas["Masculidade"] not in "MF":
            print("Erro! Tente novamente.")
    continuar = " "
    pessoas["Idade"] = int(input("Idade: "))
    contador +=1
    tidade += pessoas["Idade"]
    cadastros.append(pessoas.copy())
    print()

    while continuar not in "SN":
        continuar = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
        if continuar not in "SN":
            print("Erro! Tente novamente.")

    if continuar == "N":
        break
    print("-="*15)
print("--"*15)

print(f"Quantidade de pessoas: {contador}.")
print(f"Media de idade: {tidade/contador:.2f}.")

print(f"Mulheres: ",end="")
for pessoa in cadastros:
    if pessoa["Masculidade"] == "F":
        print(pessoa["Nome"],end=" ")

print(f"\nPessoas acima da idade de idade {tidade/contador:.2f}: ")
for pessoa in cadastros:
    if pessoa["Idade"] > (tidade/contador):
        print(f"Nome:{pessoa["Nome"]} -> Idade:{pessoa["Idade"]}")

# Exercício 95 - Aprimorando os Dicionários
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# O programa deverá permitir que o usuário cadastre vários jogadores e, depois da listagem, possa mostrar os dados de aproveitamento de cada jogador individualmente.

jogador = dict()
jogadores = list()

while True:
    jogador.clear()
    jogador["Nome"] = str(input("Nome: "))
    jogador["Partidas"] = int(input("Quantas partidas ele jogou? R: "))
    if jogador["Partidas"] == 0:
        jogador["Partidas"] = str("Não jogou.")
        jogador["gols"] = 0
    else:
        jogador["gols"] = []
        for x in range(jogador["Partidas"]):
            jogador["gols"].append(int(input(f"Quantos gols no {x+1} jogo? R: ")))
    jogador["total"] = sum(jogador["gols"])
    jogadores.append(jogador.copy())
    continuar = " "
    print()
    while continuar not in "SN":
        continuar = str(input("Quer continuar [S/N]? R: ")).strip().upper()[0]
        print()
        if continuar not in "SN":
            print("Erro! Tente novamente.")
    if continuar == "N":
        break

print("=-"*20)
print(f"{'N°':<3}{'Nome':<10}{'Gols':<20}{'Total':<5}")
for i,v in enumerate(jogadores):
    print(f"{i:<3}{v["Nome"]:<10}{str(v["gols"]):<20}{v['total']:<5}")
print("-="*20)

while True:
    escolha = " "
    escolha = int(input("Qual jogador você quer ver ? Para encerrar digite 999. \nR: "))
    if escolha == 999:
        print("Encerrado.")
        break
    elif escolha >= len(jogadores):
        print("Valor incorreto.")
        print()
    else:
        print(jogadores[escolha])
        print()