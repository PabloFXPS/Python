'''Començando com as tuplas. (OBS: Durante a execução do programa não é possivel alterar os valores)'''

lanchesimples = "Xtudo"
lanche = "Xtudo","Suco","Refri" #os valores são: 0,1,2. Para mostar basta colocar[0]

print(lanche[0:2] ,"/", lanchesimples)
for comida in lanche:
    print(f"{comida}")
#ou
for cont in range(0,len(lanche)):
    print(f"{lanche[cont]} na posição {cont}")

print(sorted(lanche)) #< mostra em ordem 

#junção de tuplas
a= (5,4,3,2)
b=(1,-1,-2,-3)
c= a+b
print (c.count(2))#mostra quantas vezes apareceu (2)
print (c.index(5))#mostra a posição (5) a primeira vez se colocar (5, 1) < ele começa a contas dps do 2° digito

pessoa = ("Gustavo", 39,"M",99.88)#funciona normal 
#para apagar a tupla toda é del(pessoa)
print(pessoa)



'''Listas[]. Diferente das tuplas elas são mutaveis, da para adicionar e remover itens enquanto o programa roda.'''

lanche = ["comida 1","comida 2", "comida 3",'comida 4']
lanche[3] = "picole" #<- da para adicionar assim, ele entra na posição que foi colocado
lanche.append("cookie") #<- adiciona no final da lista
lanche.insert(0,"quente") #<- adiciona na posicição 0 e move o resto para o lado

#APAGAR

del lanche[3] #deleta o item na posição 3
lanche.pop(3) #deleta o ultimo e da para colocar a posição que vai ser deletado
lanche.remove("picole") #deleta o "picole" ou parametro que foi passado 
lanche.clear()

#condição
if "cookie" in lanche:
    lanche.remove("cookie")

#criando com a função list
valores = list(range(4,11)) #4,5,6,7,8,9,10
valores.sort #ordena do menor para o maior
valores.sort (reverse=True) #inverte
len(valores) 

#print
valor = [1,2]
for v in valor:
    print (f"{v}.",end="")

#com posição e escolhendo o numero
for cont in range(0,5):
    valor.append(int(input("\nDigite um valor: ")))

for c,v in enumerate(valor):
    print(f"Na posição {c} tem {v}")
print("fim") 

#copia e lista
a = [3,4,5,6] #se vc colocar b=a ele vai fazer uma lição entre essas lista. Caso, vc mude B tambem vai mudar A
b = a[:]#maneira correta de se copiar. Agora, a e b não são ligado e b pode ser alterado separadamente
b[2]=3
print(f"Lista A: {a}")
print(f"Lista B: {b}")

#lista dentro de lista
dados = list()
pessoas = []

dados.append("Pedro", 25)
pessoas.append(dados[:])#A lista pessoa vai receber todos os dados da lista dados
#ou          0    1  -   0    1  -   0     1
pessoas=[["Pedro",25],["joao",22],["Maria",20]]
#              0           1            2
print(pessoas[0][0])#Mostra "Pedro"
print(pessoas[1][1])#Mostra 22 da lista joao
print(pessoas[1])#Mostra joao 22

for p in pessoas:
    print(p[0])


'''Dicionarios'''

dados = {'nome':"Pedro",'idade':25}
print(dados["nome"])
print(dados["idade"])

#adiciona um novo ELEMENTO
dados['sexo']= 'M'

#apaga um ELEMENTO eo seu Valor
del dados['idade']

#ex
filme ={'titulo':'Star Wars','ano':1977,'diretor':'Georger Lucas'}
#valores
print(filme.values()) # <- mostra os VALORES 'Star Wars, 1977, Georger Lucas'

#elementos / chaves
print(filme.keys()) # <- mostra os Valores titulo, ano, diretor

#tudo junto
print(filme.items())# <- mostra os valores e os elementos

#laços de repetição 
for k,v in filme.items():
    print(f"O {k} é {v}")

#dicionario dentro de lista
brasil = list()
estado1= {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2= {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)

#ex
estado= dict()
brasil= list()

for c in range (0,3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla: "))
    brasil.append(estado.copy()) #cria uma copia para nao ficar tudo igual
print(brasil)