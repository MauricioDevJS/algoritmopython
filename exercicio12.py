def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    try:
        temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

        temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
        print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit:.2f} °F")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número válido.")

if __name__ == "__main__":
    main()
