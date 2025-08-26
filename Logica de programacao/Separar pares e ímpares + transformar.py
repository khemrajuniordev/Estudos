# Exercício 2 — separar pares/ímpares e transformar valores

valores = [12, 5, 8, 3, 10, 7, 6]


pares = [x for x in valores if x % 2 == 0]
impares = [x for x in valores if x % 2 != 0]


pares_quadrado = [x**2 for x in pares]
impares_triplo = [x*3 for x in impares]

print("Origem :", valores)
print("Pares  :", pares,  " | Pares²:", pares_quadrado)
print("Ímpares:", impares, " | Ímpares*3:", impares_triplo)







