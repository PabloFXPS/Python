#Simular um combate entre personagens onde um ataca o outro com dano baseado em sorte/dados. A classe abstrata Personagem gerencia vida e golpes, enquanto as subclasses Guerreiro e Mago implementam formas distintas de cura.
# ┌──────────────────────────────────┐
# │            PERSONAGEM            │
# ├──────────────────────────────────┤
# │ - nome                           │
# │ - vida                           │
# │ - ataque                         │
# │ - defesa                         │
# ├──────────────────────────────────┤
# │ + atacar()                       │
# │ + receber_dano()                 │
# │ + curar()                        │
# └────────────────┬─────────────────┘
#                  │
#           ┌──────┴───────┐
#           │              │
#           ▼              ▼
# ┌────────────────┐ ┌────────────────┐
# │    GUERREIRO   │ │      MAGO      │
# ├────────────────┤ ├────────────────┤
# │ - força        │ │ - poder_magico │
# │ - armadura     │ │ - mana         │
# ├────────────────┤ ├────────────────┤
# │ + atacar()     │ │ + atacar()     │
# │ + curar()      │ │ + curar()      │
# └────────────────┘ └────────────────┘