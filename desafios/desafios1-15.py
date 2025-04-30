'''num1 = int (input("Escreva o primeiro numero para a soma = "))
num2 = int (input("Escreva o segundo numero = "))

soma = num1 + num2

#print ('O resultado da soma é {}' .format(soma))
print ('A soma entre os numero {} e {} vale {}'.format(num1,num2,soma))'''



#n1 = int(input("Digite um numero para saber seu sucessor e antecessor: "))
#ant = n1 - 1
#suc = n1 + 1

#print ("O antecessor do numero digitado é {} e o seu sucessor é {}".format(ant,suc))

#n1 = float(input("Digite um numero para saber seu dobro, triplo e sua raiz quadrada: "))
#db = n1 * 2
#tri = n1 * 3
#rq = n1**(1/2) #ou paw(n,(1/2))

#print ("dobro {}\ntriplo {}\nraiz quadrada {}".format(db,tri,rq))

#n1 = float (input("Sua primeira nota: ") )
#n2 = float (input("Segunda nota: "))

#media = (n1 + n2)/2

#print ("Sua media é: ",media) #para deixa só um numero dps do . {:.1f}

#c = float(input("Conversão de metros para centimetro e milimetro: "))
#centi = c * 100
#mili = c * 1000

#print ("centimetros: {}\nmilimetros: {}".format(centi,mili))

#carteira = float(input("Quantos vc tem na carteira: R$"))

#dolar =float(3.27)

#conversão = carteira / dolar

#print ("A conversão deu: {:.2f}".format(conversão))

#altura = float(input("Qual a altura da parede: "))
#largura = float (input("Qual a largura: "))

#area = altura * largura

#tinta = area / 2

#print ("Area: {}\nQuantidade de baldes: {}".format(area,tinta))

#n1 = int(input("Qual o numero que vc quer ver a tabuada ? "))

#print ("",n1,"X 1 = ",(n1*1),"\n",n1, "X 2 = ",(n1*2),"\n",n1, "X 3 = ",(n1*3),"\n",n1, "X 4 = ",(n1*4),"\n",n1, "X 5 = ",(n1*5),"\n",n1, "X 6 = ",(n1*6),"\n",n1, "X 7 = ",(n1*7),"\n",n1, "X 8 = ",(n1*8),"\n",n1, "X 9 = ",(n1*9),"\n",n1, "X 10 = ",(n1*10))

# produto = float(input("Insira o valor do produto = "))

#desconto =produto - ((5/100) * produto)   

#print ("Seu produto com desconto fica = ",desconto)

#salario = int (input("Teste de aumento do salario = "))

#aumento = salario + ((15/100)* salario)

#print ("O aumento ficaria = ", aumento)

#c = float(input("informe a temperatura em f = "))
#F = ((9*c)/5)+32
#print("A converção da temperatura {}, para F fica = {}".format(c,F))

D = int(input("Quantos dias o carro foi alugado: "))
K = float(input("Quantos KM rodado: "))

total = (D * 60) + (K * 0.15)

print ("O valor a pagar é: {}".format(total))