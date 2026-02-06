frase = "Curso em Video Python"
print (len(frase)) #ver quantos caracteres tem
print(frase.count('o',0,13)) #quantas vezes apareceu O
print (frase.find('deo')) #onde começa essa sequencia de caracteres
print (frase.find('Android')) #retorna -1 se nao tiver
print('Curso' in frase ) #verifica se tem essa palavra na variável

#transformação

frase.replace('Python','Android') #substitui a palavra por outra
frase.upper() #oq é maiúsculo ele deixa e colocar o resto em maiúsculo
frase.lower() #Maiusculo para minúsculo
frase.capitalize() #Joga todos para minúsculo e deixa a primeira em maiúsculo
frase.title() #analisa cada palavra e deixa todas as primeiras letras em maiúsculo

frase.strip() #remove os espaços inútil
frase.rsplit() #remove só os últimos espaço e deixa o começo
frase.lstrip() #remove o da esquerda e deixa os últimos

#divisão

frase.split() #cria uma lista com varias caracteres e separa as frase em lista

#junção

"-".join (frase)#junta a cadeia do split com varios - entre elas
  