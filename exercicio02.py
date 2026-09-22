numero1 = int(input("Informe um número:"))
numero2 =  int(input("Informe outro número:"))

maior = 0

if numero1 > numero2:
    maior = numero1
elif numero2 > numero1:
    maior = numero2
else:
    maior = numero1

print(f"Maior número: {maior}")