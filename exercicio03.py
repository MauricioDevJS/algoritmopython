def calcular_arrecadacao_poupanca(pao, broa):
    preco_pao = 0.12
    preco_broa = 1.50

    total_pao = pao * preco_pao
    total_broa = broa * preco_broa

    total_arrecadado = total_pao + total_broa
    valor_poupanca = total_arrecadado * 0.10

    return total_arrecadado, valor_poupanca

# Entrada de dados
quantidade_paes = int(input("Digite a quantidade de pães vendidos: "))
quantidade_broas = int(input("Digite a quantidade de broas vendidas: "))

# Chamada da função para calcular a arrecadação e o valor para a poupança
arrecadado, poupanca = calcular_arrecadacao_poupanca(quantidade_paes, quantidade_broas)

# Arredondando os resultados para duas casas decimais
arrecadado = round(arrecadado, 2)
poupanca = round(poupanca, 2)

# Saída de resultados
print("Total arrecadado: R$", arrecadado)
print("Valor a ser guardado na poupança: R$", poupanca)
