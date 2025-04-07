num = int(input("Número: "))
op = 0
for i in range(1, num):
    print(f"{num}+{i}={num+i}")
    print(f"{num}-{i}={num-i}")
    print(f"{num}*{i}={num*i}")
    print(f"{num}/{i}={num/i}")
    op += 4
print("Total de operações:", op)