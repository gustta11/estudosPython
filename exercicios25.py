lista = [15,63,20,25,70]
maior = 0
segundoMaior = lista[0]

for i in lista:
    if i >= maior:
        maior = i

for i in lista:
    if i >= segundoMaior and i != maior:
        segundoMaior = i

print(maior)
print(segundoMaior)