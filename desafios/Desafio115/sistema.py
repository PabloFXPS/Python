#115a – Crie um menu interativo modularizado que permita ao usuário escolher entre opções (como cadastrar uma pessoa ou listar pessoas),
#repetindo até que o usuário opte por sair.
from time import sleep
from lib.interface import *

np = pasta_cadastro("pacientes") #cria uma pasta para armazenar os cadastro.
while True:
    resp=menu(['Ver cadastros','Novo cadastro','Sair'])
    if resp==1:
        print()
        sleep(1)
        mostrar_pacientes(np)
        sleep(3)
    elif resp==2:
        novo_cadastro(np)
        sleep(2)
    elif resp==3:
        print()
        print("Encerrando..")
        break
    sleep(3)

#115b – Implemente no menu do exercício 115a a funcionalidade de gravar e ler dados utilizando
#arquivos de texto, de forma a armazenar e recuperar os cadastros.

#115c – Finalize o projeto criando um sistema completo e modular para cadastrar pessoas
#(nome e idade) em um arquivo de texto, permitindo cadastrar novas entradas e listar todas as pessoas cadastradas.