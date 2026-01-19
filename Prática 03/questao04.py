# Programa Verificador de Ano Bissexto

print("=== VERIFICADOR DE ANO BISSEXTO ===")

try:
    # Solicita o ano ao usuário
    ano = int(input("Digite um ano: "))
    
    # Verifica se é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"\nO ano {ano} É BISSEXTO!")
    else:
        print(f"\nO ano {ano} NÃO É BISSEXTO!")
        
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido!")
    print (2026)