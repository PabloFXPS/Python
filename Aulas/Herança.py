#Herança é um relacionamento entre itens gerais(ancestrais) e tipos especificos(descendentes).

class pessoa: #Classe mãe / superclasse
    def __init__(self,nome = "", idade = 0):
        self.nome = nome
        self.idade= idade
    
    def fazer_aniversario(self):
        self.idade += 1

class Aluno(pessoa): #Classe filha / subclasse
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome,idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer a matrícula.")

class Professor(pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Professor: {self.nome} esta dando aula.")


class Funcionario(pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"Funcionario: {self.nome} acabou de bater o ponto.")