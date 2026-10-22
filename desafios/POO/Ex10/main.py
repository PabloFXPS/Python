from Cafeteira import cafe, cha, leite
def main():
    bebida = cafe()
    bebida.preparar()

    bebida1 = cha()
    bebida1.preparar()

    bebida2 = leite()
    bebida2.preparar()

if __name__ == "__main__":
    main()