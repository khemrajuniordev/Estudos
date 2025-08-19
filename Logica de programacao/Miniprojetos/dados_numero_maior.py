import sys           # sys para escrever no terminal sem pular linha
import time          # time para simular espera (sleep)
import itertools     # itertools.cycle para repetir símbolos do spinner
import os            # os para limpar a tela (estilo MS-DOS)
import random  # Importa a biblioteca 'random' para gerar números aleatórios (como se fosse um dado de verdade)
# -------------------------
# Função utilitária: limpar a tela (Windows = cls | Linux/Mac = clear)
# Exemplo da vida real: como passar um pano no quadro antes de escrever de novo
# -------------------------
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
# -------------------------
# Header com vibe MS-DOS
# Exemplo da vida real: colocar uma plaquinha bonita antes de começar o serviço
# -------------------------
def header_msdos(titulo="BEM-VINDOS AO JOGO DE DADOS"):
    print("╔" + "═" * 58 + "╗")
    print("║ {:^58} ║".format(titulo))
    print("╠" + "═" * 58 + "╣")
    print("║ {:^58} ║".format("Vamos jogar dados!"))
    print("╚" + "═" * 58 + "╝")
       
# Inicializa os pontos dos jogadores em 0
# Exemplo: é como começar uma partida de futebol com o placar zerado

# -------------------------
# Spinner (rodinha girando)
# Exemplo da vida real: como um ventilador girando enquanto você espera algo ficar pronto
# -------------------------
def spinner_preloading(duracao=3.0, mensagem="Dados rolando"):
    """
    Mostra um spinner por 'duracao' segundos.
    duracao: tempo total em segundos
    mensagem: texto à esquerda do spinner
    """
    simbolos = itertools.cycle(["|", "/", "-", "\\"])  # Ciclo infinito dos símbolos (ventilador girando)
    inicio = time.time()                                # Marca o começo (cronômetro)
    while time.time() - inicio < duracao:               # Enquanto não atingir a duração...
        s = next(simbolos)                              # Pega o próximo símbolo
        sys.stdout.write(f"\r{mensagem} {s}")           # Escreve na mesma linha (\r volta pro início da linha)
        sys.stdout.flush()                              # Garante que aparece na hora
        time.sleep(0.08)                                # Pequena pausa (ex.: 80 ms)
    sys.stdout.write("\r" + " " * (len(mensagem) + 2) + "\r")  # Limpa a linha ao terminar
    print(f"{mensagem} concluído!")                     # Mensagem final


pontos1 = 0
pontos2 = 0
header_msdos()
spinner_preloading()
# Exemplo da vida real: é como começar uma partida de futebol com o placar zerado
# Loop infinito para rodadas do jogo (só termina com 'break')
# Exemplo da vida real: rodadas de truco, que só acabam quando alguém vence
while True:
    # Gera um número secreto inteiro entre 1 e 6 para cada jogador (simula lançar os dados a cada rodada)
    dado1 = random.randint(1, 6)  # Jogador 1 lança o dado
    dado2 = random.randint(1, 6)  # Jogador 2 lança o dado
    # Condição de vitória: quem fizer 5 pontos primeiro ganha
    if pontos1 == 5:
        print(f"Jogador 1 ganhou o jogo, com total de {pontos1} pontos!")  # Mensagem de vitória
        break  # Sai do loop e termina o jogo
    elif pontos2 == 5:
        print(f"Jogador 2 ganhou o jogo, com total de {pontos2} pontos!")  # Mensagem de vitória
        break  # Sai do loop e termina o jogo

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
    print(f"Jogador 1 marcou: {pontos1} | Jogador 2 marcou: {pontos2}")
    print("═" + "═" * 90 + "═")    

# Fora do loop, imprime mensagem final com operador ternário
# Exemplo da vida real: juiz dizendo qual time venceu depois do apito final
print(f"Parabens ao jogador {1 if pontos1 == 5 else 2}!")  # Decide qual jogador venceu usando lógica condicional curta ternária
print("═" + "═" * 90 + "═") 
print("Fim do jogo!")  # Encerramento oficial