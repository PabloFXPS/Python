#from math import floor

#num1 = float (input("Digite um numero: "))

#print ("A porsao inteira do numero: {} é {}".format(num1,floor(num1)))

#===============================================================#

#from math import sqrt, pow,hypot

#Cat1 = float (input("Qual o valor do cateto 1: "))
#Cat2 = float (input("Qual o valor do cateto 2: "))

#h = sqrt((pow(Cat1,2) + pow(Cat2,2)))

#print("O valor da hipotenusa é {:.2f}".format(h))

#h = hypot(Cat1,Cat2)

#print("O valor da hipotenusa é {:.2f}".format(h))

#===============================================================#

#from math import radians, sin,cos,tan

#ang = int (input("Qual o angulo que vc quer ver o seno e o coseno: "))
 
#rad = radians(ang)

#sen = sin(rad)

#cose = cos(rad)

#ta = tan(rad)

#print ("Cos: {:.2f} \nsen: {:.2f} \ntan: {:.2f}".format(cose, sen,ta))

#===============================================================#

#import random

#a1 = str(input("Primeiro aluno: "))
#a2 = str(input("Segundo aluno: "))
#a3 = str (input("Terceiro aluno: "))
#a4 = str (input("Quarto aluno: "))

#alunos = [a1,a2,a3,a4]

#escolhido = random.choice(alunos)

#print ("O aluno escolhido foi: {} ".format(escolhido))

#random.shuffle(alunos)

#print ("A sequencia é: {}".format(alunos))

#===============================================================#

#colocar o arquivo mp3 na mesma pasta e rodar o codigo a seguir:

#import pygame
#pygamer.init()
#pygamer.mixer.music.load('nome do arquivo')
#pygamer.mixer.music.play()
#pygame.event.wait()