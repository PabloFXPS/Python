#101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        print(f"Você tem {idade} anos. Não vota.")
    elif 17 <= idade <= 65:
        print(f"Você tem {idade} anos. Voto Obrigatório.")
    else:
        print(f"Você tem {idade} anos. Voto Opcional.")

nas = int(input("Em que ano você nasceu: "))
voto(nas)

#102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#o primeiro que indique o número a calcular e o outro chamado show,
#que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n,show=False):
    """
    - Fatorial de um número
    :param n: recebe o número a ser fatorado.
    :param show: (opcional) Mostra o resultado da conta.
    :return: recebe o valor do fatorial do N.
    """
    r = n
    while n > 1:
        if show:
            print(n, end=' ')
            if n > 2:
                print(f"x ",end="")
            else:
                print(f"x 1 = {r}")
        r = r * (n-1)
        n -= 1
    return r

show = True
resultado=fatorial(n=int(input("Valor a ser fatorado: ")), show=bool(input("Quer ver a conta ? [True/False]: ")))
if not show:print(resultado)

def fatorial2(n):
    """
    fatorial 2 com a biblioteca MATH
    :param n: Recebe o valor a ser fatorado.
    :return: recebe o resultado do fatorial.
    """
    from math import factorial
    re = factorial(n)
    return re
test = fatorial2(int(input("Digite o valor a ser fatorado: ")))
print(f"RESULTADO: {test}")

#103 - Faça um programa que tenha uma função chamada ficha(),
#que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome="",gols = ""):
    """
    :param nome: Recebe o nome do jogador.
    :param gols: Recebe a quantidade de gols feito.
    :return: n/a
    """
    if nome == "": nome = "<desconhecido>"
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols=0
    print(f"o jogador {nome} fez {gols} gol(s) no campeonato.")

ficha(nome=str(input("Nome do jogador: ")),gols=input("Qual foi o números de gols: "))

#104 - Crie um programa que tenha a função leiaInt(),
#que vai funcionar de forma semelhante à função input() do Python,
#só que fazendo a validação para aceitar apenas um valor numérico inteiro.
def LeiaInt(num):
    """
    :param num: Recebe o valor digitado pelo usuário.
    :return: Retorna o valor se ele for um número inteiro.
    """
    while True:
        if num.isnumeric():
            return int(num)
        else:
            print("\033[0;31mERRO 406. Tente Novamente com número inteiro.\033[m")
            num = input("Digite um novo número: ")
            print()
n=LeiaInt(input("Digite um número: "))
print(f"Você digitou o número {n}.")

# 105 - Faça um programa que tenha uma função notas()
#que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)