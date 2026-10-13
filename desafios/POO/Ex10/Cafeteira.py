#Criar uma estrutura de classes para uma cafeteira que faz café, chá e leite. A superclasse Bebida Quente possui métodos concretos (ferver água e preparar) e métodos abstratos (misturar e servir), que devem ser implementados pelas classes filhas.

# ┌─────────────────────────────────┐
# │          BEBIDA QUENTE          │
# ├─────────────────────────────────┤
# │ - temperatura                   │
# │ - quantidade                    │
# ├─────────────────────────────────┤
# │ + preparar()                    │
# │ # adicionar_ingrediente()       │
# │   {abstract}                    │
# └───────────────┬─────────────────┘
#                 │
#         ┌───────┼────────┐
#         │       │        │
#         ▼       ▼        ▼
# ┌────────────┐ ┌────────────┐ ┌────────────┐
# │   CAFÉ     │ │    CHÁ     │ │    LEITE   │
# ├────────────┤ ├────────────┤ ├────────────┤
# │            │ │            │ │            │
# ├────────────┤ ├────────────┤ ├────────────┤
# │+ preparar()│ │ +preparar()│ │ +preparar()│
# └────────────┘ └────────────┘ └────────────┘