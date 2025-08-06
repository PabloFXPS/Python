#110
def aumentar(num=0,taxas=0):
    aumento = int(num + (num*taxas/100))
    return moeda(aumento)

def diminuir(num = 0,taxas = 0):
    diminui = int(num - (num*taxas/100))
    return moeda(diminui)

def dobro(num = 0):
    vezes =int(num * 2)
    return  moeda(vezes)

def metade(num = 0):
    dividir=int(num / 2)
    return moeda(dividir)

def moeda(num = 0,moedas = "R$"):
     return f"{moedas}{num:.2f}".replace(".",",")

def taxa(num=0):
    return f"{num}%"

def resumo(num =0,taxas=0):
    print("-"*30)
    print(f"Calculo do Valor".center(30))
    print("-"*30)
    print(f"Preço:{moeda(num):>24}")
    print(f"Taxa:{taxa(taxas):>25}\n")

    print(f"Dobro:{dobro(num):>24}")
    print(f"Metade:{metade(num):>23}")
    print(f"Aumento:{aumentar(num,taxas):>22}")
    print(f"Diminuindo:{diminuir(num,taxas):>19}")
    print("-"*30)