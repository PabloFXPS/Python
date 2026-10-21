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
        resultado = self.qtd_lados ** 2
        print(f"Quadrado - Área: {resultado}")

    def perimetro(self):
        resultado = self.qtd_lados * 4
        print(f"Quadrado - Perímetro: {resultado}")

class Circulo(Poligono):
    def __init__(self, qtd_lados):
        super().__init__(qtd_lados)
        self.qtd_lados = qtd_lados

    def area(self):
        resultado = pi * (self.qtd_lados ** 2)
        print(f"Circulo - Área: {resultado:.1f}")

    def perimetro(self):
        resultado = 2 * pi * self.qtd_lados
        print(f"Circulo - Perímetro: {resultado:.1f}")

class triangulo(Poligono):
    def __init__(self, qtd_lados):
        super().__init__(qtd_lados)
        self.qtd_lados = qtd_lados

    def area(self):
        resultado = (3 ** 0.5 / 4) * (self.qtd_lados ** 2)
        print(f"Triângulo - Área: {resultado:.1f}")

    def perimetro(self):
        resultado = self.qtd_lados * 3
        print(f"Triângulo - Perímetro: {resultado:.1f}")
