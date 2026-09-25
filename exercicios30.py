array = [10,15,20,20]
elementosUnicos = []
count = 1

for i in range(0,len(array),1):
    for j in range(0,len(array),1):
        if array[i] == array[j] and i != j:
            count+=1
    if count == 1:
        elementosUnicos.append(array[i])
    count = 1

print(elementosUnicos)