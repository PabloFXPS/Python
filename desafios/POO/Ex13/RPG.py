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

