from temperature_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
)

def main():
    print("=== Conversor de Temperatura ===")
    print("Escolha a conversão:")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Fahrenheit → Kelvin")
    print("6. Kelvin → Fahrenheit")

    try:
        opcao = int(input("Digite o número da opção desejada: "))
        valor = float(input("Digite o valor da temperatura: "))
    except ValueError:
        print("Entrada inválida. Tente novamente com números.")
        return

    try:
        if opcao == 1:
            resultado = celsius_to_fahrenheit(valor)
            print(f"{valor} °C = {resultado:.2f} °F")
        elif opcao == 2:
            resultado = fahrenheit_to_celsius(valor)
            print(f"{valor} °F = {resultado:.2f} °C")
        elif opcao == 3:
            resultado = celsius_to_kelvin(valor)
            print(f"{valor} °C = {resultado:.2f} K")
        elif opcao == 4:
            resultado = kelvin_to_celsius(valor)
            print(f"{valor} K = {resultado:.2f} °C")
        elif opcao == 5:
            resultado = fahrenheit_to_kelvin(valor)
            print(f"{valor} °F = {resultado:.2f} K")
        elif opcao == 6:
            resultado = kelvin_to_fahrenheit(valor)
            print(f"{valor} K = {resultado:.2f} °F")
        else:
            print("Opção inválida.")
            return
    except ValueError as e:
        print(f"Erro: {e}")
        return


if __name__ == "__main__":
    main()