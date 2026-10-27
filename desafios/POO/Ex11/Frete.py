#Desenvolver classes para calcular fretes baseados em distância para diferentes veículos: Moto (frete livre), Caminhão (mínimo de 50 km) e Drone (máximo de 10 km). A classe Transporte deve ser abstrata e definir o método calcular frete.
# ┌─────────────────────────────────┐
# │          TRANSPORTE             │
# ├─────────────────────────────────┤
# │ - distância                     │
# │ - frete                         │
# ├─────────────────────────────────┤
# │ + calcular_frete() {abstract}   │
# └───────────────┬─────────────────┘
#                 │
#         ┌───────┼─────────┐
#         │       │         │
#         ▼       ▼         ▼
# ┌───────────┐ ┌───────────┐ ┌───────────┐
# │   MOTO    │ │ CAMINHÃO  │ │   DRONE   │
# ├───────────┤ ├───────────┤ ├───────────┤
# │+fator=0.50| |+fator=1.20| |+fator=9.50|
# ├───────────┤ ├───────────┤ ├───────────┤
# │ + calcular│ │ + calcular│ │ + calcular│
# │   _frete()│ │   _frete()│ │   _frete()│
# └───────────┘ └───────────┘ └───────────┘
#    Livre         Min 50km      Max 10km
from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia, frete):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calcular_frete(self):
        pass




class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia, 0)
        self.fator = 0.50

    def calcular_frete(self):
        self.frete = self.distancia * self.fator
        return self.frete 

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia, 0)
        self.fator = 1.20

    def calcular_frete(self):
        if self.distancia < 50:
             raise ValueError ("Distância mínima para caminhão é de 50 km.")
        else:
            self.frete = self.distancia * self.fator
            return self.frete

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia, 0)
        self.fator = 9.50

    def calcular_frete(self):
        if self.distancia > 10:
            raise ValueError("Distância máxima para drone é de 10 km.")
        else:
            self.frete = self.distancia * self.fator
            return self.frete