vogais = "aeiouAEIOU"
palavra = str(input("Informe uma palavra:"))
count = 0

for i in range(0, len(palavra)):
    if palavra[i] in vogais:
        count+= 1

print(f"A palavra tem {count} vogais")

