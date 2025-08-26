# Exercício 1 — estatísticas básicas de uma lista de números


numeros = [10, 7, 3, 20, 7, 15]


soma = sum(numeros)  

media = soma / len(numeros) if numeros else 0

menor = min(numeros) if numeros else None
maior = max(numeros) if numeros else None

crescente = sorted(numeros)
decrescente = sorted(numeros, reverse=True)

print("Lista:", numeros)
print("Soma:", soma, " | Média:", media)
print("Menor:", menor, " | Maior:", maior)
print("Ordenada ↑:", crescente)
print("Ordenada ↓:", decrescente)
