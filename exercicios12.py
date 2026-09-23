palavra = str(input("Informe uma palavra:"))
palavraInvertida = ""

for i in range(len(palavra)-1, -1, -1):
    palavraInvertida += palavra[i]

if palavra == palavraInvertida:
    print("É Palíndromo")
else:
    print("Não é palíndromo")

