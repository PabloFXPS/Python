#maneira 'inline'
print ("\033[4;31;41mOla, mundo!\033[m")
print ("\033[7;30:40mNegativo\033[m")

#colocar pelo format
nome = 'pablo'
print ("Ola! {}{}{} .".format('\033[0;31;42m', nome,'\033[m'))


#com variaveis
limpar = '\033[m'
cores = {
'azul' : '\033[34m',
'amarelo' : '\033[33m',
'pretoebranco' : '\033[7;30:40m'
}

print("{}Testando{} maneras de colocar {}cores{}.".format(cores['azul'],limpar,cores['pretoebranco'],limpar))