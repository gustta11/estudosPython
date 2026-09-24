palavra1 = str(input("Informe a primeira palavra:")).replace(" ","")
palavra2 = str(input("Informe a segunda palavra")).replace(" ","")
palavra2Ivenrtida = palavra2[::-1]


if palavra1 == palavra2Ivenrtida:
    print("É anagrama")
else:
    print("Não é anagrama")


