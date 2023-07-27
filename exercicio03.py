def calcular_arrecadacao_poupanca(pao, broa):
    preco_pao = 0.12
    preco_broa = 1.50

    total_pao = pao * preco_pao
    total_broa = broa * preco_broa

    total_arrecadado = total_pao + total_broa
    valor_poupanca = total_arrecadado * 0.10

    return total_arrecadado, valor_poupanca

quantidade_paes = int(input("Digite a quantidade de pães vendidos: "))
quantidade_broas = int(input("Digite a quantidade de broas vendidas: "))


arrecadado, poupanca = calcular_arrecadacao_poupanca(quantidade_paes, quantidade_broas)


arrecadado = round(arrecadado, 2)
poupanca = round(poupanca, 2)


print("Total arrecadado: R$", arrecadado)
print("Valor a ser guardado na poupança: R$", poupanca)
