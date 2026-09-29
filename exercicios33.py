lista = [20,25,20,35]

lista.sort()

alvo = int(input("Informe um valor:"))

for i in range(0, len(lista), 1):
    if alvo == lista[i]:
        print(f"Numero encontrado, posicao {i}")
        break