# 1) Validador de Senha Simples
# Peça ao usuário uma senha e valide se ela tem pelo menos 8 caracteres, contém letras minúsculas, maiúsculas, números e um símbolo. Se não atender, informe o que falta e peça novamente.
# Lógica:
# Ler a senha digitada.
# Inicializar “flags” para cada requisito (minúscula, maiúscula, dígito, símbolo).
# Percorrer os caracteres e marcar as flags que forem satisfeitas.
# Verificar tamanho e todas as flags.
# Se faltar algo, listar faltas e repetir; senão, aprovar e encerrar.


while True:

    senha = input("Digite sua senha: ")

    # iniciar as flags todas falsas
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    # percorrer os caracteres e marcar as flags
    for snh in senha:
        if not has_lower and snh.islower():
            has_lower = True
        elif not has_upper and snh.isupper():
            has_upper = True
        elif not has_digit and snh.isdigit():k
            has_digit = True
        elif not has_symbol and (not snh.isalnum()) and (not snh.isspace()):
            has_symbol = True

        # se já tiver todos, pode parar a varredura
        if has_lower and has_upper and has_digit and has_symbol:
            break

    # verificar tamanho e todas as flags em acumular faltas
    faltas = []

    if len(senha) < 8:
        faltas.append("pelo menos 8 caracteres")
    if not has_lower:
        faltas.append("uma letra minúscula (a-z)")
    if not has_upper:
        faltas.append("uma letra maiúscula (A-Z)")
    if not has_digit:
        faltas.append("um número (0-9)")
    if not has_symbol:
        faltas.append("um símbolo ex: !@#$%&*")

    # se estiver faltando algo após a verificação, imprimir para o usuário
    if faltas:
        print("\nSenha inválida. Está faltando:")
        for item in faltas:
            print("-", item)
        print("Tente novamente.\n")
        # volta para o while ao topo para pedir outra senha
    else:
        print("Senha válida! Todos os requisitos foram atendidos.")


# “oi! me passa sua senha?”
# enquanto você pensa, o porteiro já prepara quatro bandeirinhas mentais, todas abaixadas: minúscula, maiúscula, número e símbolo. a de tamanho ele checa no final.

# você digita. agora o porteiro faz uma revista rápida, caractere por caractere:

# “é minúscula? beleza, levanta a bandeirinha de minúscula.”

# “é maiúscula? show, sobe a de maiúscula.”

# “é número? ok, marca a de número.”

# “não é letra nem número e também não é espaço? ótimo, isso é símbolo, sobe a última.”

# se todas as quatro bandeirinhas já estiverem levantadas, ele pensa: “já vi de tudo que precisava, posso parar de conferir o resto.”

# acabou a revista? ele mede a senha: “tem pelo menos 8 caracteres?”
# agora ele monta um checklist do que faltou. pode ser: “faltou minúscula”, “faltou símbolo”, “faltou tamanho”… o que for.

# se faltou algo: ele fala com jeitinho:
# “❌ senha inválida. está faltando: … (lista o que falta). tenta de novo?”
# e volta pro começo, pedindo outra senha.

# se não faltou nada: ele sorri e carimba:
# “✅ senha válida! todos os requisitos foram atendidos.”
# e a história termina aí.

# exemplo rápido de cena:
# você digita “Senha@2025”. o porteiro encontra minúscula (“enha”), maiúscula (“S”), número (“2025”), símbolo (“@”) e conta 10 caracteres. todas as bandeirinhas sobem. carimbo de aprovado.