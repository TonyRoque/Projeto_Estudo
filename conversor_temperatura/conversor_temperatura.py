 # conversor_temperatura.py

# Funções de conversão
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def celsius_para_kelvin(c):
    return c + 273.15

# Função principal com menu
def main():
    while True:
        print("\n=== Conversor de Temperatura ===")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Celsius para Kelvin")
        print("0. Sair")

        opcao = input("Escolha uma opção (1/2/3/0): ")

        if opcao == '0':
            print("Encerrando o conversor. Até mais!")
            break

        # Validação de entrada
        try:
            temp = float(input("Digite a temperatura: "))
        except ValueError:
            print("Erro: digite um número válido.")
            continue

        # Processamento da escolha
        if opcao == '1':
            resultado = celsius_para_fahrenheit(temp)
            print(f"{temp}°C = {resultado:.2f}°F")
        elif opcao == '2':
            resultado = fahrenheit_para_celsius(temp)
            print(f"{temp}°F = {resultado:.2f}°C")
        elif opcao == '3':
            resultado = celsius_para_kelvin(temp)
            print(f"{temp}°C = {resultado:.2f}K")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

