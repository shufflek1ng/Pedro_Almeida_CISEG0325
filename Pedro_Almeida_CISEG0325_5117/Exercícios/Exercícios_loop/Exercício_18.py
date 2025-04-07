num=int(input("Num:"))
cont = 0

for n in range(1, num + 1):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    if soma == n:
        print(f"{n} é perfeito")
        cont += 1

print(f"Números perfeitos até {num}: {cont}")