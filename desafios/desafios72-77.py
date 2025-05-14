# 72 crie um programa que tenha uma tupla preenchida com uma contagem por extenso, de 0 até 20.
# o programa deverá ler um numero pelo teclado e mostrá-lo por extenso.
'''num = (
    "zero","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)
n = 0
while True:
    n = int(input("Digite um numero de 0 a 20: "))
    if 0 <= n <=20:
        break
    else:
        print("Valor incorreto.", end=" ")        
print(f"O numero esculhido foi: {num[n]}")'''


# 73 crie uma tupla com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol. na ordem de colocação depois mostre:
# a) apenas os 5 primeiros colocados
# b) os ultimos 4 
# c) uma lista em ordem alfabetica
# d) em que posição na tabela esta o time da chapecoense
'''
brasileirao_2019 = (
    "Flamengo", "Santos", "Palmeiras", "Grêmio", "Athletico-PR", "São Paulo", "Internacional",
    "Corinthians", "Fortaleza", "Goiás", "Bahia", "Vasco da Gama", "Atlético-MG", "Fluminense",
    "Botafogo", "Ceará", "Cruzeiro", "CSA", "Chapecoense", "Avaí"
)

print(f"Os 5 primeiros:{brasileirao_2019[0:5]}")
print("=-="*10)
print(f"Os ultimos 4 times:{brasileirao_2019[-4:]}")
print("=-="*10)
print(f"Em ordem alfabetica:{sorted(brasileirao_2019)}")
print("=-="*10)
print(f"Onde esta o time da chapecoense:{brasileirao_2019.index("Chapecoense")+1}°")
'''

# 74 crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. depois o menor e o maior
'''
from random import sample
#tupla corretamente Num = (randint(0,10), radint(0,10, +3x)) < para os numeros nao repetir uma o sample. 
num = sample(range(0,10),5)
maior = max(num)
menor = min(num)
tuplanum = tuple(num) #Transforma em uma tupla
print(f"Lista gerada:{tuplanum}")
print(f"Maior numero: {maior}\nMenor numero: {menor}")
'''

# 75 desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final mostre:
# a)quantas vezes apareceu o valor 9
# b)em que posição foi digitado o primeiro valor 3
# c)quase foram os numero pares
