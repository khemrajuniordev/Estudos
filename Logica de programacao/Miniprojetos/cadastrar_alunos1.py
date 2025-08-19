# 🔹 Cadastro de Alunos
# O programa pede nome e nota dos alunos
# No final, mostra a lista e a média da turma

alunos = []  # Lista para armazenar dicionários com nome e nota

while True:  # Loop para cadastrar alunos
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":  # Se o usuário digitar "sair", o loop é interrompido
        break

    nota = float(input(f"Digite a nota do aluno {nome}: "))
    alunos.append({"nome": nome, "nota": nota})  # Guarda cada aluno como dicionário

print("\n📋 Alunos cadastrados:")
soma = 0
for aluno in alunos:
    print(f"- {aluno['nome']} → Nota: {aluno['nota']}")
    soma += aluno["nota"]

if alunos:  # Se houver alunos cadastrados
    media = soma / len(alunos)
    print(f"\n📊 Média da turma: {media:.2f}")
else:
    print("Nenhum aluno cadastrado.")