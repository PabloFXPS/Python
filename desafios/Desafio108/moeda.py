#108

def aumentar(num=0,taxa=0):
    aumento = num + (num*taxa/100)
    return aumento

def diminuir(num = 0,taxa = 0):
    diminui = num - (num*taxa/100)
    return diminui

def dobro(num = 0):
    vezes = num * 2
    return vezes

def metade(num = 0):
    dividir = num / 2
    return dividir

def moeda(num = 0,moeda = "R$"):
     return f"{moeda}{num:.2f}".replace(".",",")

def taxa(num=0):
    return f"{num}%"