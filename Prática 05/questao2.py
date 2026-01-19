def verificar_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    
    Parâmetros:
    texto (str): A palavra ou frase a ser verificada
    
    Retorna:
    str: "Sim" se for palíndromo, "Não" se não for
    """
    # Remove espaços, pontuação e converte para minúsculas
    texto_limpo = ''.join(caractere.lower() for caractere in texto 
                         if caractere.isalnum())
    
    # Verifica se é igual ao seu inverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Testes da função
if __name__ == "__main__":
    print("=== TESTES DE PALÍNDROMOS ===")
    print("-" * 40)
    
    # Lista de testes
    testes = [
        "arara",
        "ovo",
        "radar",
        "Ame o poema",
        "A base do teto desaba",
        "Socorram-me, subi no ônibus em Marrocos",
        "Anotaram a data da maratona",
        "python",
        "casa",
        "hello world"
    ]
    
    # Executa os testes
    for texto in testes:
        resultado = verificar_palindromo(texto)
        print(f"'{texto}' → {resultado}")

