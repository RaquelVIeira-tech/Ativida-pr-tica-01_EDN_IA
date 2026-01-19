# Sistema de Registro de Notas - Versão Simples

def calcular_media_turma():
    print("=== SISTEMA DE REGISTRO DE NOTAS ===")
    print("=" * 40)
    
    alunos = []
    notas = []
    
    # Coleta dados dos alunos
    while True:
        nome = input("\nDigite o nome do aluno (ou 'fim' para terminar): ")
        
        if nome.lower() == 'fim':
            break
        
        try:
            nota = float(input(f"Digite a nota de {nome} (0-10): "))
            
            if 0 <= nota <= 10:
                alunos.append(nome)
                notas.append(nota)
                print(f"✅ Nota de {nome} registrada: {nota}")
            else:
                print("❌ Nota deve estar entre 0 e 10!")
                
        except ValueError:
            print("❌ Digite uma nota válida!")
    
    # Verifica se há alunos registrados
    if not alunos:
        print("\nNenhum aluno registrado.")
        return
    
    # Calcula a média
    media_turma = sum(notas) / len(notas)
    
    # Exibe resultados
    print("\n" + "="*50)
    print("RELATÓRIO DA TURMA")
    print("="*50)
    
    print("\nALUNOS E NOTAS:")
    print("-" * 30)
    for i in range(len(alunos)):
        print(f"{alunos[i]:20} → {notas[i]:5.1f}")
    
    print("\n" + "="*50)
    print(f"Total de alunos: {len(alunos)}")
    print(f"Média da turma: {media_turma:.2f}")
    
    # Estatísticas adicionais
    maior_nota = max(notas)
    menor_nota = min(notas)
    aprovados = sum(1 for nota in notas if nota >= 6)
    
    print(f"Maior nota: {maior_nota:.1f}")
    print(f"Menor nota: {menor_nota:.1f}")
    print(f"Alunos aprovados (nota ≥ 6): {aprovados}/{len(alunos)}")
    
    # Situação da média
    if media_turma >= 7:
        situacao = "Boa média! "
    elif media_turma >= 5:
        situacao = "Média regular "
    else:
        situacao = "Média baixa! Precisa melhorar "
    
    print(f"Situação: {situacao}")
    print("="*50)

# Executa o sistema
calcular_media_turma()