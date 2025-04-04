quantidade_primos = 0
numero = 2

print("Os 10 primeiros números primos são:")

while quantidade_primos < 10:

    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    
    if divisores == 2:  
        print(numero, end=" ")
        quantidade_primos += 1
    
    numero += 1