frase = "Curso em Video Python"
#print (len(frase)) #ver quantos caracteres tem
#print(frase.count('o',0,13)) #quantas vezes apareceu O
#print (frase.find('deo')) #onde começa essa sequencia de caracteres
#print (frase.find('Android')) #retorna -1 se nao tiver
#print('Curso' in frase ) #verifica se tem essa palavra na variavel

#transformação

frase.replace('Python','Android') #substitui a palavra por outra
frase.upper() #oq é maiusculo ele deixa e colocar o resto em maiusculo
frase.lower() #Maiusculo para minusculo
frase.capitalize() #Joga todos para minusculo e deixa a primeira em maiusculo
frase.title() #analisa cad a palavra e deixa todoas as primeiras letras em maiusculo

frase.strip() #remove os espaços inutil
frase.rsplit() #remove só os ultimos espaço e deixa o começo
frase.lstrip() #remove o da esquerda e deixa os ultimos

#divisão

frase.split() #cria uma lista com varias caracteres e separa as frase em lista

#junção

"-".join (frase)#junta a cadeia do split com varios - entre elas
  