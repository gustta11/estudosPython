numero1 = int(input("Informe um número:"))
numero2 = int(input("Informe outro número:"))
operacao = input("Informe qual operação deseja fazer");

if(operacao == "+"):
    print(f"{numero1 + numero2}")
elif(operacao == "-"):
    print(f"{numero1 - numero2}")
elif(operacao == "*"):
    print(f"{numero1 * numero2}")
elif(operacao == "/"):
    print(f"{numero1 / numero2}")
else:
    print("Esse operador não existe")


    