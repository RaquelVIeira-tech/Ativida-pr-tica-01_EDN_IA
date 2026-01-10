# Conversor de Moeda
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("=== QUESTÃO 1: CONVERSOR DE MOEDA ===")
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Taxa do dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do euro: R$ {taxa_euro:.2f}")
print(f"Valor em dólares: US$ {round(valor_dolar, 2):.2f}")
print(f"Valor em euros: € {round(valor_euro, 2):.2f}")
print("=" * 40)