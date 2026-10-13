from Poligono import Circulo, Quadrado, triangulo

def main():
    p1 = Quadrado(12)
    p2 = Circulo(12)
    p3 = triangulo(12)

    p1.area()
    p1.perimetro()
    p2.area()
    p2.perimetro()
    
    p3.area()
    p3.perimetro()


if __name__ == "__main__":
    main()