idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Idade inválida! Por favor, digite um valor positivo.")
elif idade <= 12:
    print("Criança (0-12 anos)")
elif idade <= 17:
    print("Adolescente (13-17 anos)")
elif idade <= 59:
    print("Adulto (18-59 anos)")
else:
    print("Idoso (60 anos ou mais)")