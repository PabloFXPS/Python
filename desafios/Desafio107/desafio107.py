#107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use algumas dessas funções.
from moeda import aumentar,diminuir,dobro,metade
valor = int(input("Digite o preço: R$"))
taxa = int(input("Quantos % vai ser a taxa? R: "))
print()

print(f"Aumentado {taxa}%, temos R${aumentar(valor,taxa)}.")
print(f"Diminuindo {taxa}%, temos R${diminuir(valor,taxa)}.")
print(f"O dobro de {valor} é R${dobro(valor)}.")
print(f"A metade de {valor} é R${metade(valor)}")