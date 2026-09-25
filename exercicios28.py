lista = [0,1,0,3,12]
novaLista = []
count = 0

for i in lista:
    if i != 0:
        novaLista.append(i)
    else:
        count+=1

for i in range(count):
    novaLista.append(0)

print(novaLista)




