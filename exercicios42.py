lista = [2,8,5,4]
menor = 0

for i in range(0,len(lista),1):
    menor = i
    for j in range(0 + i,len(lista), 1):
        if lista[j] < lista[menor]:
            menor = j
    lista[i], lista[menor] = lista[menor], lista[i]

print(lista)
