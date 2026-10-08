#109 - Modifique as funções criadas no desafio 107 para que elas aceitem um parâmetro a mais,
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from moeda import *
forma = ""
valor = int(input("Digite o preço: R$"))
imposto = int(input("Quantos % vai ser a taxa? R: "))

while forma != "SN":
    forma = str(input("Você deseja que os números mostrem formatados? [S/N]\nR:")).strip().upper()[0]
    if forma == "N" or forma == "S":
        break

if forma == "S":
    ftd = True
if forma == "N":
    ftd = False

print()

print(f"Aumentado {taxa(imposto,ftd)} de {moeda(valor,ftd)} -> Resultado: {aumentar(valor,imposto,ftd)}")
print(f"Diminuindo {taxa(imposto,ftd)} de {moeda(valor,ftd)} -> Resultado: {diminuir(valor,imposto,ftd)}")
print(f"O dobro de {moeda(valor,ftd)} é -> {dobro(valor,ftd)}")
print(f"A metade de {moeda(valor,ftd)} é -> {metade(valor,ftd)}")
