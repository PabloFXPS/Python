#Crie a classe Livro, que simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura.
from time import sleep
from rich import print
class Livro:
    def __init__(self, nome,quantidade_paginas):
        self.nome = nome
        self.quantidade_paginas = quantidade_paginas
        self.pagina_atual=1

        print(f"Abrindo...")
        sleep(1)
        print(f"Você esta na pagina 1 de {self.quantidade_paginas} do livro {self.nome}.")

    def avancar_paginas(self, passar=1):
        cont = 0
        for pg in range(0,passar,1):
            if not self.final():
                self.pagina_atual+=1
                sleep(0.5)
                print(f"Pag{self.pagina_atual}",end=" > ")
                cont+=1
        print(f"Você agora esta na pagina > {self.pagina_atual} de {self.quantidade_paginas}.")
        if self.final():
            print("Chegou ao final do livro.")
            sleep(1)
            print("Fechando...")

    def final(self)->bool:
        return True if self.pagina_atual==self.quantidade_paginas else False


l1 = Livro("Mentes Ansiosas", 40)
l1.avancar_paginas(20)
l1.avancar_paginas(10)
l1.avancar_paginas(20)
