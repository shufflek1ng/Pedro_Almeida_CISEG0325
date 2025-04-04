numero = int(input("Digite um número inteiro: "))
divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print(f"{numero} é um número PRIMO.")
else:
    print(f"{numero} NÃO é um número primo.")