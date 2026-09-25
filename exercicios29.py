lista1 = [1,2,3,4] 
lista2 = [3,4,5,6]
intersecao = []

for i in lista1:
    if i in lista1 and i in lista2:
        intersecao.append(i)

print(intersecao)