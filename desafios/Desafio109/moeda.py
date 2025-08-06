#109
def aumentar(num=0,taxas=0,formata=False):
    aumento = int(num + (num*taxas/100))
    return aumento if formata is False else moeda(aumento)

def diminuir(num = 0,taxas = 0,formata=False):
    diminui = int(num - (num*taxas/100))
    return diminui if formata is False else moeda(diminui)

def dobro(num = 0,formata=False):
    vezes = int(num * 2)
    return vezes if formata is False else moeda(vezes)

def metade(num = 0,formata=False):
    dividir = int (num / 2)
    return dividir if formata is False else moeda(dividir)

def moeda(num = 0,formata = True,moedas = "R$"):
     return f"{num}" if not formata else f"{moedas}{num:.2f}".replace(".",",")

def taxa(num=0,formata=False):
    return f"{num}" if formata is False else f"{num}%"