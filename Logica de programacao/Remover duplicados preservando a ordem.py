# Exercício 3 — deduplicar mantendo a ordem original

itens = ["maçã", "uva", "maçã", "banana", "uva", "pera"]
vistos = set()          # "carimbo" de já visto (busca O(1))
sem_duplicatas = []     # resultado

for item in itens:
    if item not in vistos:   # só entra o primeiro de cada
        vistos.add(item)     # marca como visto
        sem_duplicatas.append(item)

print("Original      :", itens)
print("Sem repetição :", sem_duplicatas)
