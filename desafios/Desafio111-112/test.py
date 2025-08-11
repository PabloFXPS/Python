#111 -Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados moeda e dado.
#Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para esse novo pacote, garantindo que tudo continue funcionando.

from UtilidadesFX.Moedas import *
valor = int(input("Digite o preço: R$"))
imposto = int(input("Quantos % vai ser a taxa? R: "))
resumo(valor,imposto)

#112 - Dentro do pacote utilidadesCev que criamos no desafio 111, temos um módulo chamado dado.
#Crie uma função chamada leiaDinheiro() que funcione como a função input(), mas com validação, aceitando apenas valores que representem quantias monetárias.

from UtilidadesFX import Dado,Moedas
valor = Dado.leiadinheiro("Digite um Valor: R$")
imposto = Dado.leiataxas("Quantos % de taxa? R:")
Moedas.resumo(valor,imposto)

#Ainda pode dar erro se mistura letras com números ex: R200-200d-2o0.