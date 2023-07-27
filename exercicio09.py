def calcular_valor_arrecadado(qtd_pequenas, qtd_medias, qtd_grandes):
    preco_pequena = 10
    preco_media = 12
    preco_grande = 15

    valor_arrecadado = (qtd_pequenas * preco_pequena) + (qtd_medias * preco_media) + (qtd_grandes * preco_grande)
    return valor_arrecadado

def main():
    try:
        qtd_pequenas = int(input("Digite a quantidade de camisetas pequenas vendidas: "))
        qtd_medias = int(input("Digite a quantidade de camisetas médias vendidas: "))
        qtd_grandes = int(input("Digite a quantidade de camisetas grandes vendidas: "))

        valor_total = calcular_valor_arrecadado(qtd_pequenas, qtd_medias, qtd_grandes)
        print(f"O valor arrecadado com a venda das camisetas é: R${valor_total:.2f}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar valores inteiros válidos.")

if __name__ == "__main__":
    main()
