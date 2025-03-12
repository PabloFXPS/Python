#import math #importa toda à biblioteca matematica 
from math import sqrt,floor #importa algo especifico da biblioteca math
num = int (input("digite um numero: "))
raiz = sqrt(num)

print('A raiz de {} é: {}'.format(num, floor(raiz)))