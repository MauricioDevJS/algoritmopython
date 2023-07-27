def calcular_litros_gasolina(preco_litro, valor_pagamento):
    litros = valor_pagamento / preco_litro
    return litros


preco_litro = float(input("Digite o preço do litro da gasolina: "))
valor_pagamento = float(input("Digite o valor do pagamento: "))


litros_gasolina = calcular_litros_gasolina(preco_litro, valor_pagamento)


print(f"Você conseguirá colocar {litros_gasolina:.2f} litros no tanque.")