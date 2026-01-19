# Verificador de Senha - Critérios Básicos

def verificar_senha(senha):
    """
    Verifica se uma senha atende aos critérios básicos de segurança
    Retorna: (bool, mensagem)
    """
    
    problemas = []
    
    # Critério 1: Comprimento mínimo
    if len(senha) < 8:
        problemas.append("❌ Muito curta (mínimo 8 caracteres)")
    
    # Critério 2: Letra maiúscula
    if not any(c.isupper() for c in senha):
        problemas.append("❌ Precisa de pelo menos 1 letra maiúscula")
    
    # Critério 3: Letra minúscula
    if not any(c.islower() for c in senha):
        problemas.append("❌ Precisa de pelo menos 1 letra minúscula")
    
    # Critério 4: Dígito numérico
    if not any(c.isdigit() for c in senha):
        problemas.append("❌ Precisa de pelo menos 1 número")
    
    # Critério 5: Caractere especial
    especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?~"
    if not any(c in especiais for c in senha):
        problemas.append("❌ Precisa de pelo menos 1 caractere especial")
    
    # Verifica se passou em todos os critérios
    if not problemas:
        return True, "✅ Senha segura! Atende a todos os critérios."
    else:
        mensagem = "Problemas encontrados:\n" + "\n".join(problemas)
        return False, mensagem

def main():
    print("=" * 50)
    print("VERIFICADOR DE SEGURANÇA DE SENHA")
    print("=" * 50)
    
    print("\nCritérios para senha segura:")
    print("1. Mínimo 8 caracteres")
    print("2. Pelo menos 1 letra maiúscula")
    print("3. Pelo menos 1 letra minúscula")
    print("4. Pelo menos 1 número")
    print("5. Pelo menos 1 caractere especial: !@#$%^&*()_+-=[]{}|;:,.<>?~")
    
    while True:
        print("\n" + "-" * 50)
        senha = input("\nDigite sua senha (ou 'sair' para encerrar): ")
        
        if senha.lower() == 'sair':
            print("Programa encerrado. Até logo! 🔒")
            break
        
        # Verifica a senha
        valida, mensagem = verificar_senha(senha)
        
        print(f"\n{'='*30}")
        print("RESULTADO DA VERIFICAÇÃO")
        print(f"{'='*30}")
        print(mensagem)
        
        # Força da senha (opcional)
        if valida:
            # Calcula pontuação
            pontos = 0
            if len(senha) >= 12:
                pontos += 2
            elif len(senha) >= 8:
                pontos += 1
            
            if any(c.isupper() for c in senha):
                pontos += 1
            if any(c.islower() for c in senha):
                pontos += 1
            if any(c.isdigit() for c in senha):
                pontos += 1
            if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?~" for c in senha):
                pontos += 1
            
            # Classifica a força
            if pontos >= 5:
                print("Nível de segurança: ALTO 🛡️")
            elif pontos >= 4:
                print("Nível de segurança: MÉDIO ⚠️")
            else:
                print("Nível de segurança: BAIXO 🔓")

if __name__ == "__main__":
    main()