palavra = str(input("Informe uma palavra"))
count = 1
chaves = []
valores = []

for i in range(0, len(palavra)):
    print("i:", i)
    print("letra:", palavra[i])
    print("count:", count)
    print("chaves:", chaves)
    print("valores:", valores)
    print("----------------")
    for j in range(0,len(palavra)):
        if palavra[i] == palavra[j]:
            count += 1
            if palavra[i] not in chaves:
                chaves.append(palavra[i])
        valores.append(count)
        count = 0

dicionario = dict(zip(chaves,valores))

print(dicionario)

#ainda não terminei