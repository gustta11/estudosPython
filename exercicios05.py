numero = int(input("Informe um número:"))

if numero % 4 == 0 and numero % 100 != 0 or numero % 400 == 0:
    print("Bissexto")
else:
    print("Não bissexto")