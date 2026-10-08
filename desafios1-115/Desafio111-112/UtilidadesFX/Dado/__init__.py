#112
def leiadinheiro(msg):
    while True:
        entrada= str(input(msg)).strip().replace(',','.')
        if entrada.isalpha() or entrada == "":
            print(f"\033[0;31mErro!!! {entrada} não é um número. Tente novamente.\033[m")
        else:
            break
    return float(entrada)

def leiataxas(taxas):
    while True:
        taxa = str(input(taxas)).strip().replace(',','.')
        if taxa.isalpha() or taxa == "":
            print(f"\033[0;32mErro!! {taxa} não é um número valido. Tente novamente.\033[m")
        else:
            break
    return float(taxa)
