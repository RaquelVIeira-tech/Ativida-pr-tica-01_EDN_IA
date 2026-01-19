# Analisador de Números Pares e Ímpares - Versão Básica

print("=== ANALISADOR DE NÚMEROS ===")
print("Classifica números como PAR ou ÍMPAR")
print("Digite '0' para terminar a entrada")
print("-" * 40)

# Contadores
contador_total = 0
contador_pares = 0
contador_impares = 0
numeros_pares = []
numeros_impares = []

while True:
    try:
        entrada = input("\nDigite um número (ou '0' para encerrar): ")
        
        # Verifica se quer sair
        if entrada.lower() == 'sair' or entrada == '0':
            break
        
        # Converte para número
        numero = float(entrada)
        
        # Verifica se é inteiro
        if numero != int(numero):
            print(f"  {numero} não é inteiro. Use números inteiros.")
            continue
        
        numero = int(numero)
        contador_total += 1
        
        # Classifica como par ou ímpar
        if numero % 2 == 0:
            contador_pares += 1
            numeros_pares.append(numero)
            print(f" {numero} é PAR")
        else:
            contador_impares += 1
            numeros_impares.append(numero)
            print(f" {numero} é ÍMPAR")
            
    except ValueError:
        print(" Por favor, digite apenas números válidos!")

# Mostra resultados
print("\n" + "="*50)
print("RESULTADOS DA ANÁLISE")
print("="*50)

print(f"\n ESTATÍSTICAS:")
print(f"Total de números digitados: {contador_total}")
print(f"Números PARES: {contador_pares}")
print(f"Números ÍMPARES: {contador_impares}")

if contador_total > 0:
    percentual_pares = (contador_pares / contador_total) * 100
    percentual_impares = (contador_impares / contador_total) * 100
    
    print(f"\n PORCENTAGENS:")
    print(f"Pares: {percentual_pares:.1f}%")
    print(f"Ímpares: {percentual_impares:.1f}%")

# Mostra as listas
if numeros_pares:
    print(f"\n NÚMEROS PARES ({len(numeros_pares)}):")
    print("   ", ", ".join(str(n) for n in sorted(numeros_pares)))

if numeros_impares:
    print(f"\n NÚMEROS ÍMPARES ({len(numeros_impares)}):")
    print("   ", ", ".join(str(n) for n in sorted(numeros_impares)))

print("\n" + "="*50)
print("Análise concluída! ")