grupoAET = "aet"
grupoANT = "nat"
grupoABT = "abt"

aet = []
ant = []
abt = []

dicionario = {}

lista = ["eat", "tea", "tan", "ate", "nat", "bat"]

def mesmasLetras(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)

for i in lista:
    if mesmasLetras(grupoAET, i):
        aet.append(i)
    elif mesmasLetras(grupoANT, i):
        ant.append(i)
    elif mesmasLetras(grupoABT,i):
        abt.append(i)

dicionario[grupoAET] = aet
dicionario[grupoANT] = ant
dicionario[grupoABT] = abt

print(dicionario)


