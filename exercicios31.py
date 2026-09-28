lista = [70,15,50,25,60]
alvo1 = int(input("Informe um numero: "))
encontrei = False

for i in range(0, len(lista), 1):
    if alvo1 == lista[i]:
        encontrei = True
        print(f"A posição é {i}")
        break
if encontrei == False:
    print("Não encontrei na lista")

# Melhor caso: O alvo está na primeira posição, encontra imediatamente
# Caso médio: O alvo está na posição intermediaria, só pecorre parte da lista
# Pior caso: O alvo está na última posição ou não existe, tem que pecorrer a lista toda 