# Programa Conversor de Temperatura

print("=== CONVERSOR DE TEMPERATURA ===")
print("Unidades disponíveis:")
print("C - Celsius")
print("F - Fahrenheit")
print("K - Kelvin")
print()

try:
    # Solicita os dados do usuário
    temperatura = float(input("Digite a temperatura: "))
    origem = input("Digite a unidade de origem (C/F/K): ").upper()
    destino = input("Digite a unidade de destino (C/F/K): ").upper()
    
    # Valida as unidades informadas
    unidades_validas = ['C', 'F', 'K']
    
    if origem not in unidades_validas or destino not in unidades_validas:
        print("Erro: Unidades devem ser C, F ou K!")
    elif origem == destino:
        print("Atenção: As unidades de origem e destino são iguais.")
        print(f"Resultado: {temperatura:.2f}°{destino}")
    else:
        resultado = 0
        
        # Conversões de Celsius para outras unidades
        if origem == 'C':
            if destino == 'F':
                resultado = (temperatura * 9/5) + 32
            elif destino == 'K':
                resultado = temperatura + 273.15
        
        # Conversões de Fahrenheit para outras unidades
        elif origem == 'F':
            if destino == 'C':
                resultado = (temperatura - 32) * 5/9
            elif destino == 'K':
                resultado = (temperatura - 32) * 5/9 + 273.15
        
        # Conversões de Kelvin para outras unidades
        elif origem == 'K':
            if destino == 'C':
                resultado = temperatura - 273.15
            elif destino == 'F':
                resultado = (temperatura - 273.15) * 9/5 + 32
        
        # Exibe o resultado formatado
        print(f"\n{temperatura:.2f}°{origem} = {resultado:.2f}°{destino}")
        
except ValueError:
    print("Erro: A temperatura deve ser um valor numérico!")