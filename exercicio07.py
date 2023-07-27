def calcular_dias_passados(dia, mes):
    if mes < 1 or mes > 12:
        raise ValueError("Mês inválido. Deve ser um valor entre 1 e 12.")
    
    if dia < 1 or dia > 30:
        raise ValueError("Dia inválido. Deve ser um valor entre 1 e 30.")
    
    dias_passados = (mes - 1) * 30 + dia
    return dias_passados

def main():
    try:
        dia = int(input("Digite o dia (entre 1 e 30): "))
        mes = int(input("Digite o mês (entre 1 e 12): "))

        dias_passados = calcular_dias_passados(dia, mes)
        print(f"Desde o início do ano até a data informada, passaram-se {dias_passados} dias.")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
