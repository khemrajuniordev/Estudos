# ================================================
# 🎯 Jogo do Número Secreto (1 a 20)
# Analogia da vida real:
# Pense que há um "tesouro" escondido com um número de 1 a 20.
# Cada palpite é como procurar o tesouro: se você está muito à esquerda (número baixo),
# eu digo "MAIOR" (vá mais à direita). Se está muito à direita (número alto),
# eu digo "MENOR" (volte um pouco). Você vence quando pisa exatamente no X do mapa!
# ================================================

import random  # Importa a biblioteca 'random' para gerar números aleatórios

# Gera um número secreto inteiro entre 1 e 20 (inclusive)
numero_secreto = random.randint(1, 20)  # Ex.: pode sair 7, 13, 20...

# Inicializa um contador de tentativas para medir quantos palpites o jogador fez
tentativas = 0  # Começa em zero porque ainda não houve palpites

# Mensagens iniciais para orientar o jogador
print("🎲 Bem-vindo ao Jogo do Número Secreto!")  # Dá as boas-vindas
print("💡 Dica: o número está entre 1 e 20.")      # Define o intervalo
print("Digite apenas números inteiros. Vamos lá!\n")  # Orienta sobre o formato de entrada

# Loop principal do jogo: continua até o jogador acertar
while True:  # 'True' significa que o loop é infinito até a gente usar 'break'
    # Tenta ler um palpite válido do usuário
    entrada = input("👉 Seu palpite: ")  # Lê o que o usuário digitou como texto (string)

    # Validação básica: checar se a entrada é número inteiro
    if not entrada.isdigit():  # Se o texto não for composto só por dígitos...
        print("⚠️ Por favor, digite um número inteiro válido (ex.: 7).")  # Aviso de erro
        continue  # Volta para o início do loop e pede novamente

    # Converte o texto para número inteiro
    palpite = int(entrada)  # Agora temos um número para comparar com o secreto

    # Verifica se o palpite está dentro do intervalo permitido (1 a 20)
    if palpite < 1 or palpite > 20:  # Se for menor que 1 ou maior que 20...
        print("⚠️ O número deve estar entre 1 e 20. Tente de novo.")  # Pede para corrigir
        continue  # Volta para pedir outro palpite

    # Se chegou aqui, o palpite é válido; contamos a tentativa
    tentativas += 1  # Soma 1 ao total de palpites realizados

    # Compara o palpite com o número secreto
    if palpite < numero_secreto:  # Se o palpite é MENOR que o secreto...
        # Analogia: você está "antes" do X do mapa → avance mais
        print("🔼 MAIOR! O número secreto é mais alto do que isso.")  # Dá dica para subir
    elif palpite > numero_secreto:  # Se o palpite é MAIOR que o secreto...
        # Analogia: você passou do X do mapa → volte um pouco
        print("🔽 MENOR! O número secreto é mais baixo do que isso.")  # Dá dica para descer
    else:
        # Se não é menor nem maior, então é IGUAL → jogador acertou!
        print(f"🎉 Parabéns! Você acertou: {numero_secreto}.")  # Mensagem de vitória
        print(f"🧮 Tentativas utilizadas: {tentativas}")         # Mostra quantas tentativas
        # Analogia final: você achou o X do mapa no {tentativas}º passo
        print("🗺️ Analogia: você encontrou o 'X' do mapa! Missão cumprida.")
        break  # Sai do loop e encerra o jogo
