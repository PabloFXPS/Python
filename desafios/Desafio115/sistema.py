#115a – Crie um menu interativo modularizado que permita ao usuário escolher entre opções (como cadastrar uma pessoa ou listar pessoas),
#repetindo até que o usuário opte por sair.
from time import sleep
from lib.interface import *

while True:
    resp=menu(['Ver cadastros','Novo cadastro','Sair'])
    if resp==1:
        print("Escolheu opção 1.")
    elif resp==2:
        print("Escolheu opção 2.")
    elif resp==3:
        print()
        print("Encerrando..")
        break
    sleep(2)