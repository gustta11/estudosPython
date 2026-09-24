palavra = "aaabbccccd" 
count = 0
countTxt = ""
compressao = ""

for i in palavra:
    for j in palavra:
        if i == j and i not in compressao:
            count += 1
    if i not in compressao:
        compressao += i
        countTxt = str(count)
        compressao += countTxt
    count = 0

print(compressao)