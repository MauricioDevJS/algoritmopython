def calcular_dias_de_vida(nome, idade):
    dias_por_ano = 365
    dias_de_vida = idade * dias_por_ano
    return dias_de_vida

# Entrada de dados
nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))

# Chamada da função para calcular os dias de vida
dias_de_vida = calcular_dias_de_vida(nome, idade)

# Saída de resultados
print(f"{nome.upper()}, VOCÊ JÁ VIVEU {dias_de_vida} DIAS")
