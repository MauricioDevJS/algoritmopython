def calcular_pagamento_amigos(valor_total_conta):
    valor_carlos_e_andre = 33.00 * 2
    valor_felipe = valor_total_conta - valor_carlos_e_andre
    valor_individual = valor_felipe / 3
    return valor_individual

def main():
    try:
        valor_total_conta = float(input("Digite o valor total da conta: "))

        if valor_total_conta < 66.00:
            print("O valor total da conta deve ser maior ou igual a R$66,00 para que todos paguem ao menos R$33,00.")
        else:
            valor_individual = calcular_pagamento_amigos(valor_total_conta)
            valor_carlos_e_andre = 33.00

            print(f"Carlos deve pagar: R${valor_carlos_e_andre:.2f}")
            print(f"André deve pagar: R${valor_carlos_e_andre:.2f}")
            print(f"Felipe deve pagar: R${valor_individual:.2f}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um valor numérico válido.")

if __name__ == "__main__":
    main()
