palavra = "aabbcdde"
count = 0

for i in palavra:
    for j in palavra:
        if i == j:
            count += 1
    if count == 1:
        print(i)
        break
    else:
        count = 0
