def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
    
    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
    
    Retorna:
    float: O valor da gorjeta calculada
    """
    # Converte a porcentagem para decimal e calcula a gorjeta
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso:
if __name__ == "__main__":
    # Teste da função
    conta = 150.00  # R$ 150,00
    porcentagem = 15  # 15% de gorjeta
    
    resultado = calcular_gorjeta(conta, porcentagem)
    print(f"Valor da conta: R$ {conta:.2f}")
    print(f"Porcentagem da gorjeta: {porcentagem}%")
    print(f"Valor da gorjeta: R$ {resultado:.2f}")
    print(f"Valor total (conta + gorjeta): R$ {conta + resultado:.2f}")
    # Testando a função com diferentes valores
testes = [
    (100.00, 10),   # 10% de R$100 = R$10
    (75.50, 15),    # 15% de R$75.50 = R$11.33
    (200.00, 20),   # 20% de R$200 = R$40
    (50.00, 0),     # 0% de R$50 = R$0
]

print("Testes da função calcular_gorjeta:")
print("-" * 40)

for conta, porcentagem in testes:
    gorjeta = calcular_gorjeta(conta, porcentagem)
    print(f"Conta: R${conta:6.2f} | Gorjeta: {porcentagem:3}% | Valor: R${gorjeta:6.2f}")