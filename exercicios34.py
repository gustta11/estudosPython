lista = [20,25,20,35]

lista.sort()

alvo = int(input("Informe um valor:"))

ocorrencia = 1


for i in range(0, len(lista), 1):
    for j in range(0, len(lista),1):
        if(lista[i] == lista[j] and i != j):
            print(f"Segunda ocorrencia: {j}")
            break;