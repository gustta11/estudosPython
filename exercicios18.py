frase = str(input("Coloque uma frase de sua preferência:"))
fraseSeparada = frase.split()
maiorPalavra = " "

for i in fraseSeparada:
   if len(i) >= len(maiorPalavra):
      maiorPalavra = i

print(maiorPalavra)