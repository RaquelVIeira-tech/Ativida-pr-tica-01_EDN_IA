def calcular_desconto(preco_original, percentual_desconto):
    """
    Calcula o valor do desconto e o preço final de um produto.
    
    Parâmetros:
    preco_original (float): Preço original do produto
    percentual_desconto (float): Porcentagem de desconto (ex: 15 para 15%)
    
    Retorna:
    tuple: (valor_desconto, preco_final) ambos arredondados para 2 casas decimais
    """
    # Calcula o valor do desconto
    valor_desconto = preco_original * (percentual_desconto / 100)
    
    # Calcula o preço final
    preco_final = preco_original - valor_desconto
    
    # Arredonda para 2 casas decimais (centavos)
    valor_desconto = round(valor_desconto, 2)
    preco_final = round(preco_final, 2)
    
    return valor_desconto, preco_final

# Programa principal
def main():
    print("=" * 50)
    print("   CALCULADORA DE DESCONTO DE PRODUTO   ")
    print("=" * 50)
    
    try:
        # Entrada do usuário
        preco_original = float(input("\nDigite o preço original do produto: R$ "))
        percentual_desconto = float(input("Digite o percentual de desconto (ex: 15 para 15%): "))
        
        # Verifica valores válidos
        if preco_original <= 0:
            print("\n❌ Erro: O preço original deve ser maior que zero!")
            return
        
        if percentual_desconto < 0 or percentual_desconto > 100:
            print("\n❌ Erro: O desconto deve estar entre 0% e 100%!")
            return
        
        # Calcula desconto
        valor_desconto, preco_final = calcular_desconto(preco_original, percentual_desconto)
        
        # Exibe resultados formatados
        print("\n" + "=" * 50)
        print("         RESUMO DA COMPRA         ")
        print("=" * 50)
        print(f"Preço original:      R$ {preco_original:>10.2f}")
        print(f"Desconto ({percentual_desconto:.1f}%):      R$ {valor_desconto:>10.2f}")
        print("-" * 50)
        print(f"Preço final:         R$ {preco_final:>10.2f}")
        print("=" * 50)
        
        # Informações adicionais
        economia_percentual = (valor_desconto / preco_original) * 100
        print(f"\n💡 Você economizou: {economia_percentual:.1f}% do valor original")
        
    except ValueError:
        print("\n❌ Erro: Digite valores numéricos válidos!")

# Executa o programa
if __name__ == "__main__":
    main()