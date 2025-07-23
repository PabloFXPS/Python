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
