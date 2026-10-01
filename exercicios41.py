lista = [5, 2, 8, 1, 4]

for j in range(0, len(lista) - 1, 1):
        for i in range(0, len(lista) - 1 - j):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

print(lista)