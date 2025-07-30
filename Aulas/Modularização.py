#Modularização

#Dividir um programa grande, aumentar a legibilidade e facilitar a manutenção.
#Ex:
#from Modularização2 import fatorial, dobro, triplo
#from Modularização2 import *
import Modularização2 #importa todas as funções da outra pasta.

num = int(input("Digite um numero inteiro: "))
fat = Modularização2.fatorial(num)
print(f"O fatorial de {num} é {fat}.")

#Pacote

#Caso, tenha muitas funções numa pasta. Da para dividir em Pacotes parte com um nome data, cores, números.
#Deve ser usado quando REALMENTE tiver MUITAS funções. Para importar > from Modularização2 import data.
#Para cada uma das pastas deve ter um arquivo __init__.py.
from PacoteEX import Numeros

print(f"O dobro de {num} é {Numeros.dobro(num)}")
print(f"O triplo de {num} é {Numeros.triplo(num)}")