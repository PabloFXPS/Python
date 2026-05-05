#Abstração é a prática de ignorar o irrelevante a se focar estritamente no essencial.

from AbstraçãoClasses import Aluno,Professor,Funcionario
 
a1 = Aluno("José",18,"Informática","A1")
a1.fazer_aniversario()
a1.fazer_matricula()

p1 = Professor("Xavier",40,"Português","Mestrado")
p1.fazer_aniversario()
p1.dar_aula()

f1 = Funcionario("Maria",30,"Secretária","Secretaria")
f1.bater_ponto()
f1.fazer_aniversario()

a1.estudar()
p1.estudar()
f1.estudar()