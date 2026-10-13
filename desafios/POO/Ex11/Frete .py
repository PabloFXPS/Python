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
# │           │ │           │ │           │
# ├───────────┤ ├───────────┤ ├───────────┤
# │ + calcular│ │ + calcular│ │ + calcular│
# │   _frete()│ │   _frete()│ │   _frete()│
# └───────────┘ └───────────┘ └───────────┘
