num1=0
num2=0

num1=int(input("Digite o 1º número: "))
num2=int(input("Digite o 2º número: "))

if num1>num2:
    print(f"Ordem Decrescente:\n {num1} ----> {num2}")
elif num2>num1:
    print(f"Ordem Crescente:\n {num1} ----> {num2}")
else:
    print("Os números são iguais, execute o código novamente.")