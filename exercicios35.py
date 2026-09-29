lista = [20,25,20,35]

lista.sort()

contador = 0

for i in range(0, len(lista), 1):
    for j in range(0, len(lista),1):
        if lista[i] == lista[j]:
            contador+=1
    print(f"Letra {lista[i]} aparece {contador} vezes")
    contador = 0