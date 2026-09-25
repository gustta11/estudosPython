lista = [20,30,25,35,26,17]


for i in range(len(lista) // 2):
    lista[i],lista[len(lista) -1 - i] = lista[len(lista) -1 - i],lista[i]
    
    
print(lista)