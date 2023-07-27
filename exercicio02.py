def calcular_quantidade_ferraduras(quantidade_cavalos):
    return 4 * quantidade_cavalos

def main():
    try:
        quantidade_cavalos = int(input("Digite a quantidade de cavalos comprados: "))

        if quantidade_cavalos <= 0:
            print("A quantidade de cavalos deve ser um valor positivo maior que zero.")
        else:
            quantidade_ferraduras = calcular_quantidade_ferraduras(quantidade_cavalos)
            print(f"Quantidade de ferraduras necessárias: {quantidade_ferraduras}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro válido.")

if __name__ == "__main__":
    main()
