#Operadores Matemáticos
# + , - , / , * , ** , // <- divisão de inteiro , ** -> expoente, % <- módulo devolve o resto de uma divisão

'''
num1=0
num2=0
total=0

num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))

total =num1/num2
print("Total da Divisão:", total)

total =num1*num2
print("Total da Multiplicação:", total)

total =num1-num2
print("Total da Subtração:", total)

total =num1+num2
print("Total da Soma:", total)

total =num1//num2
print("Total da Divisão por inteiro:", total)

total =num1**num2
print("Total do Expoente:", total)

'''

#Operadores Lógicos
#Compara dois números ou strings e devolve sempre ou True ou False
# == <- Igual a, != <- Diferente de , > - maior que , < - menor que , >= - maior ou igual , <= - menor ou igual
#Booleanos
'''
print (type(2>3)(2>3))

print (type(2<3)(2<3))
'''
#_______________________________________________________//_______________________________________________________

#Condições

# if - Se a condição for verdadeira, executa o bloco de código
# elif - Se a condição anterior não for verdadeira, mas esta for, executa o bloco de código
# else - Se nenhuma das condições anteriores for verdadeira, executa o bloco de código
# Exemplo: 



# if Condição:
## 1 nível de indentação - para estruturar o código

# entre o num1, num2 e num3 quem é o maior e o menor
#num1 > num2 && num1 > num3 -> num1 é o maior
#num2 > num1 && num2 > num3 -> num2 é o maior
#num3 > num1 && num3 > num2 -> num3 é o maior
#num1 < num2 && num1 < num3 -> num1 é o menor
#num2 < num1 && num2 < num3 -> num2 é o menor
#num3 < num1 && num3 < num2 -> num3 é o menor
#num1 > num2 -> num1 é maior que num2
#num2 > num1 -> num2 é maior que num1

num1=0
num2=0
num3=0

num1=int(input("Intrud um numero 1 : "))
num2=int(input("Intrud um numero 2 : "))
num3=int(input("Intrud um numero 3 : "))

if num1>num2 or num2>num3:
        print("num 1 é o maior, num 2 é do meio,num 3 é o menor")
elif num1>num3 or num3>num2:
        print("num 1 é o maior, num 3 é do meio,num 2 é o menor")
elif num2>num1 and num1>num3:
        print("num 2 é o maior, num 1 é do meio,num 3 é o menor")
elif num2>num3 and num3>num1:
        print("num 2 é o maior, num 3 é do meio,num 1 é o menor")
elif num3>num1 and num1>num2:
        print("num 3 é o maior, num 1 é do meio,num 2 é o menor")
elif num3>num2 and num2>num1:
        print("num 3 é o maior, num 2 é do meio,num 1 é o menor")



# match case