distancia = 300  # km
combustivel = 25  # litros

consumo_medio = distancia / combustivel

print("=== QUESTÃO 4: CALCULADORA DE CONSUMO ===")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel} litros")
print(f"Consumo médio: {round(consumo_medio, 2):.2f} km/l")
print("=" * 40)