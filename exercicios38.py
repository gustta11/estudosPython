lista = [10,2,5,2,6,7,7]
dicionario = {}
count = 1
duplicado = 0

for i in range(0, len(lista),1):
    for j in range(0, len(lista),1):
        if lista[i] == lista[j] and i != j:
            count += 1
    if i not in dicionario:
        dicionario[lista[i]] = count
    count = 1

for chave, valor in dicionario.items():
    if valor == 2:
        duplicado = chave
        break

print(duplicado)

