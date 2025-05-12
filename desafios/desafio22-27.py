#22

'''nome = str(input("Qual seu nome ?")).strip()
 
print ("Minusculo:",nome.lower(),"\n","Maiusculo:",nome.upper(),"\n")

print("quantidade de letras sem espaço: ",len(nome)- nome.count(' '))

primeiroN = nome.split()
print("quantidade de letras no primeiro nome: ",len(primeiroN[0]))'''

 

#23 faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separados

'''ex: 1234

4 unidades
3 dezenas
2 centenas
1 milhar '''

#forma string(só funciona se colocar os 4 numeros)
'''num = str (input ("Digite um numero de 0 a 9999 : \n"))

print ("{}: Unidade\n{}: Dezena\n{} Centenas\n{} milhar ". format(num[3],num[2],num[1],num[0]))'''

#forma numerica
'''
num = int (input("Informe um numero: "))
unidade = num // 1 % 10 #divide tudo por 1 e tira o modulo(resto) de 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 %10

print ("{} Unidade\n{} Dezena\n{} Centenas\n{} milhar ". format(unidade,dezena,centena,milhar))'''

#24 crie um programa que leia o nome de uma cidade e diga se ele começa ou não com "santo"

'''cidade = str (input("Digite o nome da cidade: "))

city = cidade.split()

print ("Verificação para saber se sua cidade tem santo no começo do nome: ", 'santo' in city[0].lower())'''

#25 crie um programa que leia o nome de uma pessoa e diga se tem silva no nome

'''nome = str (input("Qual o seu nome: "))

print("Seu nome tem silva : ", 'Silva' in nome.title())'''

#26 faça um programa que leia uma frase e mostre : quantas vezes aparece a letra "A" em posição ela parece em primeiro e quando ela aparece em ultimo
'''
frase = str(input("Digite uma frase: "))
frase = frase.lower().strip()
print ("Quantidade de vezes que a letra 'a' apareceu {}\n posição do primeiro a: {}\n ultima vez: {} ".format(frase.count('a'), frase.find('a')+1,frase.rfind('a')+1))'''

#27 faça um programa que leia o nome de uma pessoa completo e mostre o primeiro e ultimo nome

'''ex > ana maria de Souza
primeiro > ana 
ultimo > souza '''

'''nome = str(input("Digite seu nome completo: ")).title().split()

print ("seu primerio nome: '{}' \nseu ultimo nome: '{}' ".format(nome[0],nome[len(nome)-1]))'''
