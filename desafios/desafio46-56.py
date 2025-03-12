# 46 faça um programa que mostre a contagem regressiva para o estouro de fogos de artificio. 
# 10 até 0 com pausa de 1s entre eles.
'''
from time import sleep

print("Contagem para os fogos: ")
for x in range (10,-1,-1):
    print (x)
    sleep(1)
print('🎆🎇🎉🎉')'''

# 47 crie um programa que mostre na tela todos os numeros pares que estão no intervalo de 1 até 50
'''par = []
for x in range (1,51): #for n in range(2,51,2)-print(n,end=' ')
    if x%2==0:
        par.extend([x])
print(f"Aqui esta a lista de numeros pares de 1 até 50:\n {par}")'''

#48 faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontram entre 1 até 500.
'''soma = 0
multiplos = []
for x in range (1,501,2):
    if x%3==0:
        multiplos.extend([x])
        soma += x
print(f'Multiplos: {multiplos} \nSoma: {soma}')'''

#49 refaça o desafio 9 com laços de repetição
'''n1 = int(input("TABUADA\nDigite um numero: "))

for x in range(0,11):
    print(f"{n1} X {x} = {n1*x}")
print("Fim")'''

#50 desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daquels que forem pares. se o valor foir impar desconsidera.
'''print("Digite 6 numeros.")
soma = 0
par = []
for x in range(0,6):
    num=int(input(f"{x+1}°: "))
    if num%2==0:
        par.append(num) #append > adiciona os valores
    soma = sum(par) #sum > soma todos os numeros de uma lista
print(f"Esse foram os numeros pares: {par}\nSoma deles: {soma}")'''

#51 desenvolva um programa que leia o primeiro termo e a razao de uma pa e mostre os 10 primeiros termos dessa progressao
'''resultado = []
print("Progressão aritmética\n")
rz=int(input("Qual vai ser a razão dessa PA: "))
ptm=int(input("Qual o primeiro termo: "))

print("\nResultado: ")
for x in range(10):
    termo = ptm + x *rz
    print(termo,end=",")
print("...")'''

#52 faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo
'''print("Verificação se o numero é primo.")
n=int(input("\nNumero: "))

divisores = 0

for x in range (1,n+1):
    if n % x == 0:
        divisores +=1
if divisores == 2:
    print(f"O numero {n} é primo.")
else:
    print(f"O numero {n} não é primo.")'''

#53 crie um programa que leia uma frase qualquer e diga se ela é um palindromo desconsiderando os espaços.
'''frase= str(input("Digite um frase ou palavra: ")).strip().upper()
palavras = frase.split()#separa as palavras entre 'E','X'
junto = ''.join(palavras)#junta tudo EX
inverso = ''

for letra in range(len(junto) -1,-1,-1): #pega o numero de letra e vai até a ultima letra e volta
    inverso += junto[letra]
if inverso == junto:
    print(f"{frase} é um palindromo")  
else:
    print(f"{frase} não é um palindromo")'''

#54 crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas são maior de idade e quem é menor (21 anos)
'''import os
from datetime import date
maiores = []
menores = []
mc = 0 
c = 0
anoat= date.today().year

for i in range (0,7):
    os.system("cls") #limpa o console a cada loop. Precisa da biblioteca os.

    nome = str(input(f"{i+1}° nome: "))
    idade = int(input("ano de nascimento: ")) #<- alterar para ano 
    if anoat - idade >= 21:
        c += 1
        maiores.append(nome)
    else:
        mc += 1
        menores.append(nome)
os.system("cls") #para linux é os.system("clear")    
print(f"Dos nome digitados {c} são de maior sendo eles: {maiores}.\nDos menores são {mc}, os nome são{menores}")'''

#55 faça um programa que leia o peso de cinco pessoas. no final mostre qual foi o maior e qual o menor.
'''peso = []

print("Digite o peso de 5 pessoas.")
for i in range(1,6):
    pesos= float(input(f"{i}° Peso: "))
    peso.append(pesos)

menor=min(peso)
maior=max(peso)
print(f"Dos pesos digitados o maior é {maior} e o menor {menor}.")'''

# 56 desenvolva um programa que leia o nome,idade e sexo de 4 pessoas. No final do programa mostre :
# -media de idade x
# -qual o homem mais velho
# -quantas mulheres tem menos de 20 anos

'''media = 0
midadehomem = 0
nomehvelho= ''
mulhermenor = 0
for c in range (1,5):
    print(f"---{c}° Pessoa---")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    Sexo = str(input("Sexo [M/F]: ")).strip() #da para usar o upper()
    media += idade
    if c == 1 and Sexo in 'Mm':
        midadehomem = idade
        nomehvelho = nome
    if Sexo in 'Mm' and idade > midadehomem:
        midadehomem = idade
        nomehvelho = nome
    if Sexo in 'Ff' and idade < 20:
        mulhermenor += 1
print(f"Media de idade {media/c}")
print(f"O nome do homen mais velho é {nomehvelho} com idade de {midadehomem}.")
print (f"Total de mulheres menores de 20 anos: {mulhermenor}")'''
