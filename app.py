# Função para exibir o menu principal e obter a escolha do usuário
def exibir_menu():
    print("\n=== Menu Principal ===")
    print("1. Responder perguntas do diagnóstico")
    print("2. Ver recomendações de cuidados")
    print("3. Encerrar")
    return input("Escolha uma opção (1, 2 ou 3): ").strip()

# Função para fazer uma pergunta e obter resposta sim/não
def perguntar_sintoma(pergunta, pontos):
    while True:
        resposta = input(pergunta + " (sim/não): ").strip().lower()
        if resposta == "sim":
            return pontos
        elif resposta == "não":
            return 0
        else:
            print("Por favor, responda apenas com 'sim' ou 'não'.")

# Função para realizar o diagnóstico e mostrar o resultado
def realizar_diagnostico():
    # Perguntas com seus respectivos pontos
    pontos_totais = 0
    pontos_totais += perguntar_sintoma("Você está com febre?", 20)
    pontos_totais += perguntar_sintoma("Você tem tosse?", 15)
    pontos_totais += perguntar_sintoma("Você sente dores no corpo?", 15)
    pontos_totais += perguntar_sintoma("Você tem dor de garganta?", 10)
    pontos_totais += perguntar_sintoma("Você está com congestão nasal?", 10)
    pontos_totais += perguntar_sintoma("Você sente cansaço extremo?", 30)

    # Calcular probabilidade de gripe
    probabilidade = (pontos_totais / 100) * 100  # 100 é a soma total possível de pontos

    # Exibir resultado
    print("\nResultados do Diagnóstico:")
    print(f"Probabilidade de gripe: {probabilidade}%")

    # Diagnóstico final e recomendações
    if probabilidade >= 75:
        print("Alta chance de gripe.")
        print("Recomendações: Descanse bastante, hidrate-se bem e evite contato com outras pessoas para não espalhar o vírus. Considere procurar atendimento médico, especialmente se os sintomas piorarem.")
    elif probabilidade >= 40:
        print("Moderada chance de gripe.")
        print("Recomendações: Descanse e fique atento aos sintomas. Hidrate-se bem e, se os sintomas persistirem ou aumentarem, consulte um médico.")
    else:
        print("Baixa chance de gripe.")
        print("Recomendações: Parece ser um resfriado leve ou um quadro não grave. Continue se cuidando com descanso e hidratação. Se tiver dúvidas ou se os sintomas mudarem, procure orientação médica.")
    
    # Opção de voltar ao menu ou sair
    while True:
        escolha = input("\nDigite 'menu' para voltar ao menu principal ou 'sair' para encerrar: ").strip().lower()
        if escolha == "menu":
            return True  # Voltar ao menu
        elif escolha == "sair":
            return False  # Sair do programa
        else:
            print("Escolha inválida. Digite 'menu' ou 'sair'.")

# Função para exibir recomendações gerais
def exibir_recomendacoes():
    print("\n=== Recomendações Gerais ===")
    print("- Descanse o suficiente para que o corpo possa se recuperar.")
    print("- Hidrate-se bem, bebendo bastante água e líquidos quentes.")
    print("- Mantenha-se aquecido e evite mudanças bruscas de temperatura.")
    print("- Evite contato próximo com outras pessoas para não espalhar possíveis vírus.")
    print("- Se tiver sintomas graves, como febre alta ou dificuldades para respirar, procure atendimento médico.")

# Programa principal com o menu de navegação
while True:
    opcao = exibir_menu()
    
    if opcao == "1":
        voltar_ao_menu = realizar_diagnostico()
        if not voltar_ao_menu:
            print("Encerrando o programa.")
            break
    elif opcao == "2":
        exibir_recomendacoes()
    elif opcao == "3":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")