N = int(input("Informe um número:"))
soma = 0

for i in range(1,N+1):
    soma+= i

print(f"Soma total : {soma}")

soma = N*(N+1)/2 

print(soma)