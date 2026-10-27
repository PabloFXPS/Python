from Frete import  Moto, Caminhao, Drone

def main():
    distancia = 9
    moto = Moto(distancia)
    print(f"Frete de moto com {distancia} km: R${moto.calcular_frete():.2f}")

    caminhao = Caminhao(distancia)
    try:
        print(f"Frete de caminhão com {distancia} km: R${caminhao.calcular_frete():.2f}")
    except ValueError as e:
        print(f"Erro ao calcular frete de caminhão: {e}")

    drone = Drone(distancia)
    try:
        print(f"Frete de drone com {distancia} km: R${drone.calcular_frete():.2f}")
    except ValueError as e:
        print(f"Erro ao calcular frete de drone: {e}")

if __name__ == "__main__":
    main()