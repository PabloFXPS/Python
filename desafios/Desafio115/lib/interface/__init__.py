def leiaint(msg):
    while True:
        from time import sleep
        try:
            r= int(input(msg))
            if 0 >= r or r > 3:
                print("Opção invalida.")
                sleep(2)
                continue
        except (ValueError, TypeError):
            print("Erro. Tente novamente.")
            sleep(2)
            continue
        else:
           return r

def linha(tam = 42):
    print('-' * tam)

def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()

def menu(lista):
    print()
    cabecalho('Menu de Cadastro')
    cont = 1
    for x in lista:
        print(f"{cont}-{x}")
        cont += 1
    linha()
    op = leiaint("Sua Opção: ")
    return op