# calculadora simples v2 - com repetição

# Funções das operações
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero!"

# Loop principal
def main():
    while True:
        print("\n=== Calculadora Simples ===")
        print("Operações disponíveis:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")

        operacao = input("Escolha a operação (1/2/3/4/0): ")

        if operacao == '0':
            print("Encerrando a calculadora. Até mais!")
            break  # sai do loop

        # Coleta de números
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: você deve digitar números válidos.")
            continue  # volta pro início do loop

        # Verificação da operação
        if operacao == '1':
            resultado = somar(num1, num2)
        elif operacao == '2':
            resultado = subtrair(num1, num2)
        elif operacao == '3':
            resultado = multiplicar(num1, num2)
        elif operacao == '4':
            resultado = dividir(num1, num2)
        else:
            print("Operação inválida.")
            continue  # volta pro menu

        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
