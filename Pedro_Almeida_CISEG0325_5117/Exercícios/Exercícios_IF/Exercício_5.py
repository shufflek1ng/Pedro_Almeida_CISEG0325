num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

if num1 == num2 or num1 == num3 or num2 == num3:
    print("Existem números iguais, corra o código novamente.")
else:
    
    if num1 < num2 and num1 < num3:
        if num2 < num3:
            print(f"Ordem crescente: {num1}, {num2}, {num3}")
        else:
            print(f"Ordem crescente: {num1}, {num3}, {num2}")
    elif num2 < num1 and num2 < num3:
        if num1 < num3:
            print(f"Ordem crescente: {num2}, {num1}, {num3}")
        else:
            print(f"Ordem crescente: {num2}, {num3}, {num1}")
    else:
        if num1 < num2:
            print(f"Ordem crescente: {num3}, {num1}, {num2}")
        else:
            print(f"Ordem crescente: {num3}, {num2}, {num1}")


    if num1 > num2 and num1 > num3:
        if num2 > num3:
            print(f"Ordem decrescente: {num1}, {num2}, {num3}")
        else:
            print(f"Ordem decrescente: {num1}, {num3}, {num2}")
    elif num2 > num1 and num2 > num3:
        if num1 > num3:
            print(f"Ordem decrescente: {num2}, {num1}, {num3}")
        else:
            print(f"Ordem decrescente: {num2}, {num3}, {num1}")
    else:
        if num1 > num2:
            print(f"Ordem decrescente: {num3}, {num1}, {num2}")
        else:
            print(f"Ordem decrescente: {num3}, {num2}, {num1}")