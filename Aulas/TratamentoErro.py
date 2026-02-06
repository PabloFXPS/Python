#sintaxe: Erro de trocar letras ou mal formuladas.
print(x) #NameError

#Semantico: Podem estar bem formatadas, mas não fazer aquilo que o programador quer ou mesmo nada de útil.
print(x) #NameError. X não foi declarado.

#ValueError: Atribuição de valor errada.
n = int(input("Numero: ")) #Vamos dizer que você escreveu OITO <- isso é uma string não um número inteiro.
print(n)

#ZeroDivisionError: Quando o programa tenta dividir algo por 0.
numerador = int(input("Numerador: "))
divisor = int(input("Divisor: ")) #Se colocar 0 no Denominador da função vai dar essa exceção.
r = numerador / divisor
print(f"Resultado: {r}")

#TypeError: Tipo de dado é inadequado para X função ou operação.
r = 5 / "2" #Um número sendo dividido por uma string.

#KeyError(dicionários) e IndexErro(tuplas,listas): Erros referêntes as variáveis-compostas
lst = [3,4,5]
print(lst[3]) #A lista só vai até 2 de alcance.

#ModuleNotFoundError: Modulo não encontrado.
import lua

#Referências:
#https://www.youtube.com/watch?v=xz2B3bfNjEk
#https://www.w3schools.com/python/python_ref_exceptions.asp
#https://pt.stackoverflow.com/questions/105438/qual-%C3%A9-a-diferen%C3%A7a-entre-erro-sint%C3%A1tico-e-sem%C3%A2ntico
#https://medium.com/@michelelozada/qual-a-diferen%C3%A7a-entre-valueerror-e-typeerror-no-python-60352d0c8603

#Tente.
try:
    numerador = int(input("Numerador: "))
    divisor = int(input("Divisor: "))
    r = numerador / divisor

except Exception as erro:     #Se ter falha. Erro vai receber a exceção.
    print(f"Erro foi: {erro.__cause__}") #O erro vai mostrar a causa.
except (ValueError,TypeError):
    print(f"Tivemos erro com os valores inseridos.")
except ZeroDivisionError:
    print("Não da para dividir por 0.")
except KeyboardInterrupt:
    print("O usuário encerrou o programa.")

else:       #Deu certo.
    print(f"Resultado: {r}")
finally:    #Vai executar dando certo ou errado.
    print("Volte sempre!")