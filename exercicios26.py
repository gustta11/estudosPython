lista = [1,2,2,3,4,4,5]
lista2 = []

for i in lista:
    for j in lista:
        if i == j and i not in lista2:
            lista2.append(i)


print(lista2)