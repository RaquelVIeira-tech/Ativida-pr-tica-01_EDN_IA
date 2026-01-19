from datetime import date

def calcular_dias_vida(data_nascimento):
    """
    Calcula quantos dias uma pessoa está viva.
    
    Parâmetros:
    data_nascimento (str): Data de nascimento no formato 'YYYY-MM-DD'
    
    Retorna:
    int: Número total de dias de vida
    """
    # Converte a string para objeto date
    ano, mes, dia = map(int, data_nascimento.split('-'))
    nascimento = date(ano, mes, dia)
    
    # Data atual
    hoje = date.today()
    
    # Calcula a diferença em dias
    dias_vida = (hoje - nascimento).days
    
    return dias_vida

# Testes simples
if __name__ == "__main__":
    print("Testando a função calcular_dias_vida:")
    print("-" * 40)
    
    # Teste com uma data conhecida
    nascimento = "1986-03-12"
    resultado = calcular_dias_vida(nascimento)
    print(f"Data: {nascimento} → {resultado:,} dias")
    
    # Teste com data atual (deve retornar 0 ou 1)
    hoje = date.today()
    data_hoje = hoje.strftime("%Y-%m-%d")
    resultado2 = calcular_dias_vida(data_hoje)
    print(f"Data: {data_hoje} → {resultado2} dias")