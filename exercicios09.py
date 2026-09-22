numero = int(input("Informe um número para calcular a fatorial:"))
resultado = 1

for i in  range(numero, 0, -1):
    resultado*= i

print(resultado)    