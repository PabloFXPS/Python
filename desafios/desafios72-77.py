# 72 crie um programa que tenha uma tupla preenchida com uma contagem por extenso, de 0 até 20.
# o programa deverá ler um numero pelo teclado e mostrá-lo por extenso.
num = (
    "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)
n = 0
while True:
    while n > 0 and n <=20:
        n = int(input("Digite um numero de 0 a 20: "))
        