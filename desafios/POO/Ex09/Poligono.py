#Você deve criar uma hierarquia com uma classe abstrata Polígono e subclasses como Quadrado e Círculo. Métodos como calcular_área e calcular_perímetro devem ser abstratos na classe mãe.
#          ┌──────────────────────────┐
#          │         POLÍGONO         │
#          ├──────────────────────────┤
#          │ - qtd_lados              │
#          ├──────────────────────────┤
#          │ # área()    {abstract}   │
#          │ # perímetro() {abstract} │
#          └────────────┬─────────────┘
#                       │
#             ┌─────────┴─────────┐
#             │                   │
#   ┌─────────▼─────────┐ ┌───────▼────────┐
#   │      QUADRADO     │ │     CÍRCULO    │
#   ├───────────────────┤ ├────────────────┤
#   │ - lado            │ │ - raio         │
#   ├───────────────────┤ ├────────────────┤
#   │ + área()          │ │ + área()       │
#   │ + perímetro()     │ │ + perímetro()  │
#   └───────────────────┘ └────────────────┘

from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Quadrado(Poligono):
    def __init__(self, qtd_lados):
        super().__init__(qtd_lados)
        self.qtd_lados = qtd_lados

    def area(self):
        print(f"Quadrado - Área: {self.qtd_lados ** 2}")

    def perimetro(self):
        print(f"Quadrado - Perímetro: {self.qtd_lados *4}")

class Circulo(Poligono):
    def __init__(self, qtd_lados):
        super().__init__(qtd_lados)
        self.qtd_lados = qtd_lados

    def area(self):
        print(f"Circulo - Área: {pi * (self.qtd_lados ** 2)}")

    def perimetro(self):
        print(f"Circulo - Perímetro: {2*pi * self.qtd_lados}")

class triangulo(Poligono):
    def __init__(self, qtd_lados):
        super().__init__(qtd_lados)
        self.qtd_lados = qtd_lados

    def area(self):
        print(f"Triângulo - Área: {(3 ** 0.5 / 4) * (self.qtd_lados ** 2)}")

    def perimetro(self):
        print(f"Triângulo - Perímetro: {self.qtd_lados *3}")

    