def calcular_quantidade_ingredientes(qtd_sanduiches):
    peso_queijo = 50
    peso_presunto = 50
    peso_carne = 100 

    qtd_queijo = qtd_sanduiches * 2 * peso_queijo / 1000  
    qtd_presunto = qtd_sanduiches * peso_presunto / 1000  
    qtd_carne = qtd_sanduiches * peso_carne / 1000  

    return qtd_queijo, qtd_presunto, qtd_carne

def main():
    try:
        qtd_sanduiches = int(input("Digite a quantidade de sanduíches a fazer: "))

        if qtd_sanduiches <= 0:
            print("A quantidade de sanduíches deve ser um valor positivo maior que zero.")
        else:
            qtd_queijo, qtd_presunto, qtd_carne = calcular_quantidade_ingredientes(qtd_sanduiches)
            print(f"Quantidade de queijo necessária: {qtd_queijo:.2f} kg")
            print(f"Quantidade de presunto necessária: {qtd_presunto:.2f} kg")
            print(f"Quantidade de carne necessária: {qtd_carne:.2f} kg")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro válido.")

if __name__ == "__main__":
    main()
