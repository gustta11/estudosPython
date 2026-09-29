lista = [5,1,3,7,2]
numerosSoma = []
numerosSoma2 = []
vistos = []
alvo = int(input("Informe o número: "))

for i in lista:
    for j in lista:
        if i + j == alvo and i and j not in numerosSoma:
            numerosSoma.append(i)
            numerosSoma.append(j)

print(numerosSoma)

for i in range(0,len(lista),1):
    diferenca = alvo - lista[i]
    if diferenca in vistos:
        numerosSoma2.append(diferenca)
        numerosSoma2.append(lista[i])
    else:
        vistos.append(lista[i])

    
print(numerosSoma2)
