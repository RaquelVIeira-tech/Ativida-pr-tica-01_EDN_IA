# Calculadora Básica
print("=== CALCULADORA BÁSICA ===")
print("Operações disponíveis:")
print("+ : Adição")
print("- : Subtração")
print("* : Multiplicação")
print("/ : Divisão")

# Entrada dos números
num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

# Realiza o cálculo
if operacao == '+':
    resultado = num1 + num2
    print(f"\n{num1} + {num2} = {resultado}")
    
elif operacao == '-':
    resultado = num1 - num2
    print(f"\n{num1} - {num2} = {resultado}")
    
elif operacao == '*':
    resultado = num1 * num2
    print(f"\n{num1} × {num2} = {resultado}")
    
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"\n{num1} ÷ {num2} = {resultado}")
    else:
        print("\nErro: Não é possível dividir por zero!")
        
else:
    print("\nOperação inválida! Use +, -, * ou /")