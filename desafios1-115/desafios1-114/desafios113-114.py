#113 – Reescreva a função leiaInt() do desafio 104, incluindo agora a possibilidade da digitação de um número de tipo válido.
#Crie também uma função leiaFloat() com a mesma funcionalidade.
def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f"Erro. Tente de novo!")
            continue
        except KeyboardInterrupt:
            print("\nEntrada interrompida pelo usuário.")
            break
        else:
            return n

n=LeiaInt("Digite um número Inteiro: ")
if n is not None: #Colocado para quando o usuário interromper não mostrar essa mensagem.
    print(f"Você digitou o número {n}.")

print("-=-"*15)

def LeiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print(f"Erro. Tente de novo!")
            continue
        except KeyboardInterrupt:
            print(f"Interrompida pelo usuário.")
            break
        else:
            return f

f = LeiaFloat("Digite um número Real: ")
if f is not None:
    print(f"O usuário digitou {f}.")

#114 – Crie um código em Python que teste se o site pudim.com está acessível pelo computador que está executando o script.
import urllib.error
import urllib.request

try:
    noAr = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site Pudim não esta acessível.")
else:
    print("O site pudim esta acessível.")
