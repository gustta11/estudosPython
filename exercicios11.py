palavra = str(input("Informe uma palavra:"))
palavraInvertida = ""

for i in range(len(palavra)-1,-1,-1):
    palavraInvertida += palavra[i]

print(palavraInvertida)