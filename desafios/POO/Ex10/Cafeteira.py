#Criar uma estrutura de classes para uma cafeteira que faz café, chá e leite. A superclasse Bebida Quente possui métodos concretos (ferver água e preparar) e métodos abstratos (misturar e servir), que devem ser implementados pelas classes filhas.

# ┌─────────────────────────────────┐
# │          BEBIDA QUENTE          │
# ├─────────────────────────────────┤
# │ + preparar()                    │
# │ + ferver_agua()                 |
# | + misturar() {abstract}         | 
# | + servir() {abstract}           |
# └───────────────┬─────────────────┘
#                 │
#         ┌───────┼────────┐
#         │       │        │
#         ▼       ▼        ▼
# ┌────────────┐ ┌────────────┐ ┌────────────┐
# │   CAFÉ     │ │    CHÁ     │ │    LEITE   │
# ├────────────┤ ├────────────┤ ├────────────┤
# │+misturar() | |+misturar() | |+misturar() |
# | +servir()  | |+servir()   | | +servir()  |
# └────────────┘ └────────────┘ └────────────┘

from abc import ABC, abstractmethod

class Bebidaquente(ABC):
    def preparar(self):
        self.ferver_agua()
        self.misturar()
        self.servir()

    def ferver_agua(self):
        
        return print(f"----PREPARANDO BEBIDA----\nFervendo a agua á 100°C...")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class cafe(Bebidaquente):
    def misturar(self):
        return print(f"Adicionando pó de café e coando com a água quente...")

    def servir(self):
        return print(f"Servindo o café na xícara...")

class cha(Bebidaquente):
    def misturar(self):
        return print(f"Adicionando folhas de chá e coando com a água quente...")

    def servir(self):
        return print(f"Servindo o chá na xícara...")

class leite(Bebidaquente):
    def misturar(self):
        return print(f"Misturando o leite com a água quente...")

    def servir(self):
        return print(f"Servindo o café com leite na xícara...")