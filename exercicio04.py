def calcular_dias_de_vida(nome, idade):
    dias_por_ano = 365
    dias_de_vida = idade * dias_por_ano
    return dias_de_vida


nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))


dias_de_vida = calcular_dias_de_vida(nome, idade)


print(f"{nome.upper()}, VOCÊ JÁ VIVEU {dias_de_vida} DIAS")
