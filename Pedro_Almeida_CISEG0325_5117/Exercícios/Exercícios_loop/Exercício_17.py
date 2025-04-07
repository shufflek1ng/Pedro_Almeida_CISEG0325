print("Múltiplos de 5, não de 3 (1 a 1001):")

for i in range (1,1001):
    if i % 5 == 0 and i % 3 != 0:
        print (i)