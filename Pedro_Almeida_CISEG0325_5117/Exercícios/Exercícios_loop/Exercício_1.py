contador_pares = 0
contador_impares = 0
numero = 1

print("30 PRIMEIROS NÚMEROS PARES:")
while contador_pares < 30:
    if numero % 2 == 0:
        print(numero, end=" ")
        contador_pares += 1
    numero += 1

numero = 1
print("\n\n30 PRIMEIROS NÚMEROS ÍMPARES:")
while contador_impares < 30:
    if numero % 2 != 0:
        print(numero, end=" ")
        contador_impares += 1
    numero += 1