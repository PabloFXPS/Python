from abc import ABC,abstractmethod #abstract base classes

class pessoas(ABC): #Classe mãe / superclasse  || Um classe abstrata é aquela que nao vai virar um objeto, apenas servir de base para as subclasses.
    def __init__(self,nome = "", idade = 0):
        self.nome = nome
        self.idade= idade
    
    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod #metodo abstrato
    def estudar(self):
        pass

class Aluno(pessoas): #Classe filha / subclasse
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome,idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer a matrícula.")

    def estudar(self):
        print(f"Aluno {self.nome} esta estudando para prova.")

class Professor(pessoas):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Professor: {self.nome} esta dando aula.")

    def estudar(self):
        print(f"O professor {self.nome} esta estudando para seu mestrado.")

class Funcionario(pessoas):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"Funcionario: {self.nome} acabou de bater o ponto.")

    def estudar(self):                  #< da erro se nao for colocado na subclasse
        print(f"O funcionario {self.nome} esta estudando para ser especialista.")