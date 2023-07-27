def calcular_area_terreno(comprimento, largura):
    area = comprimento * largura
    return area

def main():
    try:
        comprimento = float(input("Digite o comprimento do terreno em metros: "))
        largura = float(input("Digite a largura do terreno em metros: "))

        if comprimento <= 0 or largura <= 0:
            print("As dimensões devem ser valores positivos maiores que zero.")
        else:
            area_terreno = calcular_area_terreno(comprimento, largura)
            print(f"A área do terreno é: {area_terreno} metros quadrados.")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")

if __name__ == "__main__":
    main()
