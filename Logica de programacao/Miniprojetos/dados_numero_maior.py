import random  # Importa a biblioteca 'random' para gerar números aleatórios (como se fosse um dado de verdade)

# Inicializa os pontos dos jogadores em 0
# Exemplo: é como começar uma partida de futebol com o placar zerado
pontos1 = 0
pontos2 = 0

print("Bem-vindo ao jogo de dados!")     # Mensagem inicial (boas-vindas)
print("Vou jogar os dados juntos...")    # Explicação de que ambos jogarão ao mesmo tempo

# Loop infinito para rodadas do jogo (só termina com 'break')
# Exemplo da vida real: rodadas de truco, que só acabam quando alguém vence
while True:
    # Gera um número secreto inteiro entre 1 e 6 para cada jogador (simula lançar os dados a cada rodada)
    dado1 = random.randint(1, 6)  # Jogador 1 lança o dado
    dado2 = random.randint(1, 6)  # Jogador 2 lança o dado

    # Verifica qual dado foi maior
    if dado1 > dado2:
        # Jogador 1 ganhou a rodada
        print(f"Jogador 1 ganhou a rodada com número do dado {dado1} contra o número do dado do jogador 2: {dado2}")
        pontos1 += 1  # Adiciona 1 ponto ao jogador 1
    elif dado2 > dado1:
        # Jogador 2 ganhou a rodada
        print(f"Jogador 2 ganhou a rodada com número do dado {dado2} contra o número do dado do jogador 1: {dado1}")
        pontos2 += 1  # Adiciona 1 ponto ao jogador 2
    else:
        # Empate na rodada
        print(f"Empate na rodada com número do dado {dado1} contra o número do dado {dado2}")

    # Mostra a pontuação atualizada de cada jogador
    # Exemplo da vida real: é como o placar na tela durante um jogo de futebol
    print(f"Jogador 1: {pontos1} | Jogador 2: {pontos2}")

    # Condição de vitória: quem fizer 5 pontos primeiro ganha
    if pontos1 == 5:
        print(f"Jogador 1 ganhou o jogo, com total de {pontos1} pontos!")  # Mensagem de vitória
        break  # Sai do loop e termina o jogo
    elif pontos2 == 5:
        print(f"Jogador 2 ganhou o jogo, com total de {pontos2} pontos!")  # Mensagem de vitória
        break  # Sai do loop e termina o jogo

# Fora do loop, imprime mensagem final com operador ternário
# Exemplo da vida real: juiz dizendo qual time venceu depois do apito final
print(f"Parabens ao jogador {1 if pontos1 == 5 else 2}!")  # Decide qual jogador venceu usando lógica condicional curta ternária
print("Fim do jogo!")  # Encerramento oficial
