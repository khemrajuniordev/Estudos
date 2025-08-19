# =========================================
# ✅ Lista de Tarefas (mostra a lista a cada inclusão)
# Analogia da vida real:
# Imagine um quadro branco na parede. Cada nova tarefa é uma nova linha no quadro.
# Sempre que você escreve uma nova linha, você lê o quadro inteiro para ver tudo que já tem lá.
# =========================================

tarefas = []  # Cria a lista vazia onde vamos guardar as tarefas (o "quadro")

while True:  # Inicia um laço infinito; só saímos quando o usuário pedir
    tarefa = input("Digite uma tarefa (ou 'sair' para encerrar): ").strip()  # Lê a tarefa e remove espaços extras #strip() metodo de string que remove caracteres em branco do inicio e do fim
    if tarefa.lower() == "sair":  # Se digitou 'sair', é o sinal para parar o cadastro
        break  # Encerra o laço 'while' (parar de cadastrar)

    if not tarefa:  # Se a pessoa apertou Enter vazio...
        print("⚠️ Tarefa vazia não foi adicionada.")  # ...avisamos que não vamos adicionar
        continue  # Volta para o início do laço para pedir de novo

    tarefas.append(tarefa)  # Adiciona a tarefa válida ao final da lista (escreve no "quadro")

    print("\n📋 Lista de Tarefas:")  # Título para a listagem atual
    for t in tarefas:  # Percorre cada item já cadastrado (cada linha no "quadro")
        print(f"- {t}")  # >>> CORRIGIDO: esta linha deve estar INDENTADA, pois faz parte do 'for'
