def calcular_salario_bruto(horas_normais, horas_extras):
    valor_por_hora_normal = 10.00
    valor_por_hora_extra = 15.00

    salario_bruto = (horas_normais * valor_por_hora_normal) + (horas_extras * valor_por_hora_extra)
    return salario_bruto

def calcular_salario_liquido(salario_bruto):
    taxa_impostos = 0.10
    salario_liquido = salario_bruto * (1 - taxa_impostos)
    return salario_liquido

def main():
    try:
        horas_normais = float(input("Digite a quantidade de horas normais trabalhadas: "))
        horas_extras = float(input("Digite a quantidade de horas extras trabalhadas: "))

        salario_bruto = calcular_salario_bruto(horas_normais, horas_extras)
        salario_liquido = calcular_salario_liquido(salario_bruto)

        print(f"Salário bruto: R${salario_bruto:.2f}")
        print(f"Salário líquido: R${salario_liquido:.2f}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")

if __name__ == "__main__":
    main()
