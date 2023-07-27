def calcular_valor_a_pagar(peso_prato):
    preco_por_quilo = 12.00
    valor_a_pagar = peso_prato * preco_por_quilo
    return valor_a_pagar

def main():
    try:
        peso_prato = float(input("Digite o peso do prato montado em quilos: "))

        if peso_prato <= 0:
            print("O peso do prato deve ser um valor positivo maior que zero.")
        else:
            valor_a_pagar = calcular_valor_a_pagar(peso_prato)
            print(f"Valor a pagar: R${valor_a_pagar:.2f}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número válido.")

if __name__ == "__main__":
    main()
