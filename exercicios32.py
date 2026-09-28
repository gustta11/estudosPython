lista = [70,15,50,25,60]

lista.sort()

inicio = 0
fim = len(lista) - 1
encontrado = False

alvo = int(input(f"Informe um número: "))

while inicio <= fim:

    meio = int((inicio+fim)/2)

    if alvo == lista[meio]:
        print("Econtrado")
        encontrado = True
        break
    elif alvo > lista[meio]:
        inicio = meio + 1
    elif alvo < lista[meio]:
        fim = meio - 1
    else:
        print("Número não encontrado na lista")

if encontrado == False:
    print("Número não encontrado na lista.")

