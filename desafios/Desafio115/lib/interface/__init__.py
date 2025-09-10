import os

def pasta_cadastro(pasta):
    nome_pasta = pasta
    if not os.path.exists(nome_pasta):
        os.makedirs(nome_pasta)
        print("Pasta do cadastros criada.")
    else:
        print("Pasta de cadastros ja existente.")
    return nome_pasta

def mostrar_pacientes(pasta):
    raiz = os.getcwd()
    try:
        caminho = f'{pasta}'
        os.chdir(caminho)
    except FileNotFoundError:
        print("Pasta não encontrada!!")
    else:
        cont = 1
        cabecalho("Pacientes cadastrados")
        for files in os.listdir():
            if files.lower().endswith(".txt"):
                nomes,_ = os.path.splitext(files)
                print(f"{cont} - {nomes}")
                cont +=1
                os.chdir(raiz)

def novo_cadastro(Cpaciente):
    raiz = os.getcwd()
    os.chdir(Cpaciente)
    print()
    novc = str(input("Nome do Paciente: "))
    idade = int(input("Idade: "))
    sintomas = str(input("Sintomas do paciente: "))
    try:
        nov_cliente = novc + ".txt"
        arquivo = open(nov_cliente,"x")
        arquivo.write(f"Nome: {novc}\nIdade: {idade}\nSintomas: {sintomas}")
        arquivo.close()
    except FileExistsError:
        print("Cadastro ja existente.")
    else:
        print("\nCadastrado com sucesso.")
    os.chdir(raiz)

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