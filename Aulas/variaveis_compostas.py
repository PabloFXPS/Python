#Començando com as tuplas. (OBS: Durante a execução do programa não é possivel alterar os valores)
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