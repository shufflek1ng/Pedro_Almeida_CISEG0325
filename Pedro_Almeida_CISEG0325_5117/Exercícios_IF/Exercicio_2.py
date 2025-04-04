num1= 0
num2 = 0
num3 = 0

num1=int(input("Digite o 1º número: "))
num2=int(input("Digite o 2º número: "))
num3=int(input("Digite o 3º número: "))

if num1>num2 and num2>num3:
    print("O primeiro número é o maior e o terceiro número é o menor")
elif num1>num3 and num3>num2:
    print("O primeiro número é o maior e o segundo número é o menor" )
elif num2>num1 and num1>num3:
    print("O segundo número é o maior e o terceiro número é o menor")
elif num2>num3 and num3>num1:
    print("O segundo número é o maior e o primeiro número é o menor")
elif num3>num2 and num2>num1:
    print("O terceiro número é o maior e o primeiro número é o menor")
elif num3>num1 and num1>num2:
    print("O terceiro número é o maior e o segundo número é o menor")
else:
    print("Os números são iguais, corra o código novamente.")