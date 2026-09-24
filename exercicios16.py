palavra = "programacao" 
novaPalavra = " "


for i in palavra:
    if i not in novaPalavra:
        novaPalavra += i

print(novaPalavra)