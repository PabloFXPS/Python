# Criar uma estrutura para calcular salários, com uma superclasse abstrata Funcionário (contendo nome, salário bruto, descontos e um método para analisar o salário) e subclasses Horista e Mensalista, cada uma com sua lógica específica de cálculo.
    #                   ┌──────────────────────┐
    #                   │      FUNCIONÁRIO     │
    #                   ├──────────────────────┤
    #                   │ - nome               │
    #                   │ - matrícula          │
    #                   ├──────────────────────┤
    #                   │ + trabalhar()        │
    #                   │ + calcular_salário() │
    #                   └───────────┬──────────┘
    #                               │
    #           ┌───────────────────┼───────────────────┐
    #           │                   │                   │
    #           ▼                   ▼                   ▼
    #   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
    #   │   GERENTE    │    │  DESENVOLVEDOR│   │   ESTAGIÁRIO │
    #   ├──────────────┤    ├──────────────┤    ├──────────────┤
    #   │ - bônus      │    │ - linguagem  │    │ - faculdade  │
    #   ├──────────────┤    ├──────────────┤    ├──────────────┤
    #   │ + calcular_  │    │ + calcular_  │    │ + calcular_  │
    #   │   salário()  │    │   salário()  │    │   salário()  │
    #   └──────────────┘    └──────────────┘    └──────────────┘