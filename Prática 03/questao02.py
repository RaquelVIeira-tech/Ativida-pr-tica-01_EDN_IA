peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

if peso <= 0 or altura <= 0:
    print("Erro: Peso e altura devem ser valores positivos!")
else:
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"
    
    # Adicionando a impressão do resultado
    print(f"\nIMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")