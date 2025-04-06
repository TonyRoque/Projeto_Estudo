#função de conversão

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def celsius_para_kelvin(c):
    return c + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def fahrenheit_para_kelvin(f):
    return celsius_para_kelvin(fahrenheit_para_celsius(f))

def kelvin_para_fahrenheit(k):
    return celsius_para_fahrenheit(kelvin_para_celsius(k))

#função de conversão de temperatura e entrada para maiscula.

def converter_temperatura(valor, de_unidade, para_unidade):
    de_unidade = de_unidade.upper()
    para_unidade = para_unidade.upper()

    if de_unidade == para_unidade:
        return valor

#condicional para decisão da formula.

    if de_unidade == 'C':
        if para_unidade == 'F':
            return celsius_para_fahrenheit(valor)
        elif para_unidade == 'K':
            return celsius_para_kelvin(valor)
    elif de_unidade == 'F':
        if para_unidade == 'C':
            return fahrenheit_para_celsius(valor)
        elif para_unidade == 'K':
            return fahrenheit_para_kelvin(valor)
    elif de_unidade == 'K':
        if para_unidade == 'C':
            return kelvin_para_celsius(valor)
        elif para_unidade == 'F':
            return kelvin_para_fahrenheit(valor)

    return "Erro: Conversão inválida!"

# Parte principal do codigo, interação com o usuario.

def main():
    print("=== Conversor Inteligente de Temperatura ===")
    print("Unidades disponíveis: C (Celsius), F (Fahrenheit), K (Kelvin)")

    de_unidade = input("Digite a unidade de entrada (C/F/K): ").strip().upper()
    para_unidade = input("Digite a unidade de saída (C/F/K): ").strip().upper()

    try:
        valor = float(input("Digite o valor da temperatura: "))
    except ValueError:
        print("Erro: valor inválido!")
        return

    resultado = converter_temperatura(valor, de_unidade, para_unidade)

    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"Resultado: {valor}°{de_unidade} = {round(resultado, 2)}°{para_unidade}")


if __name__ == "__main__":
    main()

 
