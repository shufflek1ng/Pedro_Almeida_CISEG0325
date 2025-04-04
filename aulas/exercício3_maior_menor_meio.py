while True:
    num1 = int(input("Digite o número 1: "))
    num2 = int(input("Digite o número 2: "))
    num3 = int(input("Digite o número 3: "))

    if num1 == num2 and num1 == num3 and num2 == num3:
        break 
    else:
        print("Os números são iguais. Digite-os novamente.")

# número maior
if num1 > num2 and num1 > num3:
    print("O número 1 é o maior")
elif num2 > num1 and num2 > num3:
    print("O número 2 é o maior")
else:
    print("O número 3 é o maior")

# número menor
if num1 < num2 and num1 < num3:
    print("O número 1 é o menor")
elif num2 < num1 and num2 < num3:
    print("O número 2 é o menor")
else:
    print("O número 3 é o menor")

# número do meio
if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    print("O número 1 é o do meio")
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    print("O número 2 é o do meio")
elif (num3 > num1 and num3 < num2) or (num3 < num1 and num3 > num2):
    print("O número 3 é o do meio")