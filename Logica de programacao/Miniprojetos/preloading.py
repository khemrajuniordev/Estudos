# =========================
# PRELOADING ASCII SIMPLES
# =========================
# Autor: você, dev Raj :)
# Ideia: mostrar um feedback visual enquanto algo "carrega"
# (ex.: baixar dados, processar arquivos, esperar resposta de API)

import sys           # sys para escrever no terminal sem pular linha
import time          # time para simular espera (sleep)
import itertools     # itertools.cycle para repetir símbolos do spinner
import os            # os para limpar a tela (estilo MS-DOS)

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
def header_msdos(titulo="PRELOADING ASCII - MS-DOS STYLE"):
    print("╔" + "═" * 58 + "╗")
    print("║ {:^58} ║".format(titulo))
    print("╠" + "═" * 58 + "╣")
    print("║ {:^58} ║".format("Carregando..."))
    print("╚" + "═" * 58 + "╝")

# -------------------------
# Spinner (rodinha girando)
# Exemplo da vida real: como um ventilador girando enquanto você espera algo ficar pronto
# -------------------------
def spinner_preloading(duracao=3.0, mensagem="Processando"):
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

# -------------------------
# Barra de progresso
# Exemplo da vida real: encher um copo de água aos pouquinhos até completar
# -------------------------
def barra_progresso(total_passos=50, delay=0.05, largura=30, mensagem="Baixando"):
    """
    Mostra uma barra de progresso preenchendo até 'total_passos'.
    total_passos: quantos incrementos a barra terá
    delay: pausa entre cada incremento (segundos)
    largura: largura visual da barra (quantidade de blocos)
    mensagem: texto à esquerda
    """
    for passo in range(1, total_passos + 1):                # Conta de 1 até total_passos
        pct = passo / total_passos                          # Proporção concluída (0..1)
        blocos = int(pct * largura)                         # Quantos blocos cheios
        barra = "█" * blocos + "░" * (largura - blocos)     # Desenha a barra (cheio + vazio)
        sys.stdout.write(f"\r{mensagem} [{barra}] {int(pct*100):3d}%")  # Mostra a barra e %
        sys.stdout.flush()                                   # Atualiza no terminal
        time.sleep(delay)                                    # Simula trabalho acontecendo
    sys.stdout.write("\n")                                   # Pula linha ao terminar
    print(f"{mensagem} concluído!")                          # Mensagem final

# -------------------------
# Demonstração rápida
# Exemplo da vida real: cardápio com “entrada” (spinner) e “prato principal” (barra)
# -------------------------
def demo():
    limpar_tela()                                   # Limpa a tela para ficar organizado
    header_msdos("DEMO DE PRELOADING ASCII")        # Título velho estilo
    print()                                         # Linha em branco para respiro

    print("1) Spinner (3s):")
    spinner_preloading(duracao=3, mensagem="Processando arquivos")  # Rodinha por 3s
    time.sleep(0.5)

    print("\n2) Barra de progresso:")
    barra_progresso(total_passos=60, delay=0.03, largura=35, mensagem="Baixando dados")  # Copo enchendo

# -------------------------
# Ponto de entrada
# Exemplo da vida real: “se eu for o cozinheiro principal, sirvo o prato;
# se eu for apenas um ingrediente importado por outro arquivo, fico quieto”
# -------------------------
if __name__ == "__main__":
    demo()
