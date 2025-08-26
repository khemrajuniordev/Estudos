# Exercício 4 — remover todas as ocorrências de um valor, sem bug de .remove no loop

valores = [5, 7, 5, 10, 5, 3, 7]
alvo = 5

# Abordagem segura: list comprehension (cria nova lista filtrada)
filtrada = [x for x in valores if x != alvo]

print("Antes :", valores)
print(f"Removendo todas as ocorrências de {alvo} …")
print("Depois:", filtrada)
