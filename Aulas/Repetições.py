#for ou para ex: for c in range(0,3):

# for c in range(0,6):
#     print('oi')
# print('F')


# for c in range(0,6): #mostra numero da repetição
#     print(c)
# print('F')


# for c in range(0,6,-1): #conta de tras para frente
#     print(c)
# print('F')


# for c in range(0,6,2): #conta de 2 em 2
#     print(c)
# print('F')

# n = int(input("Digite um numero: ")) #le o valor e mostra os numeros até eles
# for c in range(0,n+1):
#     print(c)
# print('Fim')

# i = int(input("Inicio: "))
# f = int(input("Digite o final: "))
# p = int(input("Passos: "))
# for c in range(i,f+1,p):
#     print(c)
# print("Fim") #Selecione o começo, fim e intervalos de uma contagem

# for c in range(0,3):
#     n = int(input("Digite um valor: "))
# print("fim") #faz a variavel N repetir 3x

# s = 0
# for c in range(0,4):
#     n = int(input("Digite um numero: "))
#     s += n
# print(f'A somatória dos numeros digitados é: {s}')#Soma dos numeros

'''WHILE: enquanto a condição for true ele continua'''

# c = 1
# while c < 10:
#     print(c)
#     c += 1
# print("Fim")

# r='S' 
# while r =='S':
#     n = int(input('Digite um valor: '))
#     r = str(input("Quer continuar: [S/N]")).upper()
# print('FIM')

# n = 1
# par = impar = 0
# while n != 0:
#     n = int(input("Digite um valor: "))
#     if n !=0:
#         if n % 2 == 0:
#             par += 1
#         else:
#             impar +=1
# print (f"Dos numeros digitados: {par} são par e {impar} impar") 

'''Parar o loop'''

#para colocar um loop infinito use while true:

n = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break #< interrompe o loop
    s += n
print(f"a soma dos numero deu : {s}")