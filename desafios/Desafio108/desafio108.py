#108 - Adapte o código do desafio 107, criando uma função adicional chamada moeda()
#que consiga mostrar os valores como um valor monetário formatado.
from Desafio108.moeda import *

valor = int(input("Digite o preço: R$"))
imposto = int(input("Quantos % vai ser a taxa? R: "))
print()

print(f"Aumentado {taxa(imposto)} de {moeda(valor)} -> Resultado: {moeda(aumentar(valor,imposto))}")
print(f"Diminuindo {taxa(imposto)} de {moeda(valor)} -> Resultado: {moeda(diminuir(valor,imposto))}")
print(f"O dobro de {moeda(valor)} é -> {moeda(dobro(valor))}")
print(f"A metade de {moeda(valor)} é -> {moeda(metade(valor))}")
