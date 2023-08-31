def celsius_para_kelvin(celsius):
    return celsius + 273.15

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    graus = float(input("Digite a temperatura em graus Celsius: "))
    
    print("Escolha a conversão:")
    print("1 - Celsius para Kelvin")
    print("2 - Celsius para Fahrenheit")
    
    escolha = int(input("Digite o número da conversão desejada: "))
    
    if escolha == 1:
        resultado = celsius_para_kelvin(graus)
        unidade = "Kelvin"
    elif escolha == 2:
        resultado = celsius_para_fahrenheit(graus)
        unidade = "Fahrenheit"
    else:
        print("Escolha inválida.")
        return
    
    print(f"{graus} graus Celsius são equivalentes a {resultado} {unidade}.")

if __name__ == "__main__":
    main()
def celsius_para_kelvin(celsius):
    return celsius + 273.15

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    graus = float(input("Digite a temperatura em graus Celsius: "))
    
    print("Escolha a conversão:")
    print("1 - Celsius para Kelvin")
    print("2 - Celsius para Fahrenheit")
    
    escolha = int(input("Digite o número da conversão desejada: "))
    
    if escolha == 1:
        resultado = celsius_para_kelvin(graus)
        unidade = "Kelvin"
    elif escolha == 2:
        resultado = celsius_para_fahrenheit(graus)
        unidade = "Fahrenheit"
    else:
        print("Escolha inválida.")
        return
    
    print(f"{graus} graus Celsius são equivalentes a {resultado} {unidade}.")

if __name__ == "__main__":
    main()
