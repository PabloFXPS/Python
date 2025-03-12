'''temp = int(input("Quanto tempo tem seu carro? "))
if temp <=3:
    print ("Carro novo")
else:
    print("Carro velho")
print ("-FIM-") '''

#simplicaficado
'''print ('carro'if temp <=3 else 'carro velho')'''

#testes

'''nome = str(input("Qual seu nome? "))
if nome == 'Pablo':
    print('temos o mesmo nome.')
print('ola {}'. format(nome))

n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua segunda nota: "))
m = (n1 + n2)/2
print ('A sua media foi {:.1f}'.format(m))
if m>=6.0:
    print ("Sua media esta boa.")
else:
    print("Sua media esta ruim")'''

#condições aninhadas: elif = else e if ou senao e se 

limpar = '\033[m'
cor = {
'verm':'\033[31m',
'azul':'\033[34m',
'li':'\033[36m',
'ama':'\033[33m',
}

nome = input (str("Qual o seu nome: ")).lower()

if nome == 'gustavo':
    print ('{}Seu nome é bonito.{}'.format(cor['azul'],limpar))
elif nome == 'pedro' or nome == 'leonardo' or nome == 'claudio':
    print ('{}Seu nome é bem popular.{}'.format(cor['verm'],limpar))
elif nome == 'ana' or nome == 'jessica' or nome == 'maria':
    print('{}belo nome feminino.{}'.format(cor['li'],limpar))
else:
    print ('{}Seu nome é bem normal.{}'.format(cor['ama'],limpar))
print('{}Ola {}{}, {}tenha um bom dia.{}'.format(cor['verm'],nome,limpar,cor['azul'],limpar)) 