dicionario = {}
lista = [9,11,9,9,5,10,11,11,11]
count = 1
comparacaoValor = 0
numeroMaisAparece = 0

for i in range(0, len(lista),1):
    for j in range(0, len(lista),1):
        if lista[i] == lista[j] and i != j:
            count += 1
    if i not in dicionario:
        dicionario[lista[i]] = count
    count = 1


for chave, valor in dicionario.items():
    for c, v in dicionario.items():
        if valor > v and chave != c:
            numeroMaisAparece = chave

print(numeroMaisAparece)


