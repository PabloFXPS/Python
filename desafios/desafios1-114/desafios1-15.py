# 1. Faça um programa que some dois números inteiros e mostre o resultado.

num1 = int(input("Escreva o primeiro numero para a soma = "))
num2 = int(input("Escreva o segundo numero = "))

soma = num1 + num2

#print ('O resultado da soma é {}' .format(soma))
print ('A soma entre os numero {} e {} vale {}'.format(num1,num2,soma))


# 2. Faça um programa que leia um número e mostre seu sucessor e antecessor.
n1 = int(input("Digite um numero para saber seu sucessor e antecessor: "))
ant = n1 - 1
suc = n1 + 1
print ("O antecessor do numero digitado é {} e o seu sucessor é {}".format(ant,suc))

# 3. Faça um programa que leia um número, calcule e mostre o dobro, triplo e a raiz quadrada.
n1 = float(input("Digite um numero para saber seu dobro, triplo e sua raiz quadrada: "))
db = n1 * 2
tri = n1 * 3
rq = n1**(1/2) #ou pow(n,(1/2))
print ("dobro {}\ntriplo {}\nraiz quadrada {}".format(db,tri,rq))

# 4. Faça um programa que leia duas notas de um aluno, calcule e mostre a média.
n1 = float (input("Sua primeira nota: ") )
n2 = float (input("Segunda nota: "))
media = (n1 + n2)/2
print ("Sua media é: ",media) #para deixa só um numero dps do . {:.1f}

# 5. Leia um valor em metros e exiba convertido em centímetros e milímetros.
c = float(input("Conversão de metros para centimetro e milimetro: "))
centi = c * 100
mili = c * 1000
print ("centimetros: {}\nmilimetros: {}".format(centi,mili))

# 6. Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
carteira = float(input("Quantos vc tem na carteira: R$"))
dolar =float(3.27)
conversão = carteira / dolar
print ("A conversão deu: {:.2f}".format(conversão))

# 7. Faça um programa que leia a largura e altura de uma parede, calcule sua área e a quantidade de tinta necessária para pintá-la.
altura = float(input("Qual a altura da parede: "))
largura = float (input("Qual a largura: "))
area = altura * largura
tinta = area / 2
print ("Area: {}\nQuantidade de baldes: {}".format(area,tinta))

# 8. Faça um programa que leia um número inteiro e mostre sua tabuada.
n1 = int(input("Qual o numero que vc quer ver a tabuada ? "))
print ("",n1,"X 1 = ",(n1*1),"\n",n1, "X 2 = ",(n1*2),"\n",n1, "X 3 = ",(n1*3),"\n",n1, "X 4 = ",(n1*4),"\n",n1, "X 5 = ",(n1*5),"\n",n1, "X 6 = ",(n1*6),"\n",n1, "X 7 = ",(n1*7),"\n",n1, "X 8 = ",(n1*8),"\n",n1, "X 9 = ",(n1*9),"\n",n1, "X 10 = ",(n1*10))

# 9. Leia o preço de um produto e mostre com 5% de desconto.
produto = float(input("Insira o valor do produto = "))
desconto =produto - ((5/100) * produto)   
print ("Seu produto com desconto fica = ",desconto)

# 10. Leia o salário de um funcionário e mostre com 15% de aumento.
salario = int (input("Teste de aumento do salario = "))
aumento = salario + ((15/100)* salario)
print ("O aumento ficaria = ", aumento)

# 11. Converta uma temperatura de Celsius para Fahrenheit.
c = float(input("informe a temperatura em f = "))
F = ((9*c)/5)+32
print("A converção da temperatura {}, para F fica = {}".format(c,F))

# 12. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade

D = int(input("Quantos dias o carro foi alugado: "))
K = float(input("Quantos KM rodado: "))

total = (D * 60) + (K * 0.15)

print ("O valor a pagar é: {}".format(total))