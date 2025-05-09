def primos(x):
    if x <= 1:
        return "Não"
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return "Não"
    return "Sim"

def perfeito(x):
    sum_div = 0
    for i in range(1, x):
        if x % i == 0:
            sum_div += i
    return "Sim" if sum_div == x else "Não"

def par_impar(x):
    if x % 2 == 0:
        return "Par"
    else:
        return "Impar"

def divisores(x):
    num = 0
    for i in range(1, x+1):
        if x % i == 0:
            num += 1
    return num

def ver_numeros():
    valores = []
    
    while len(valores) <= 50:
        for _ in range(10):
            if len(valores) == 50:
                break
            try:
                valor=int(input("Digite um número entre 1 e 1000: "))
                if 1 <= valor <= 1000:
                    valores.append(valor)
                else:
                    print("Erro! Valor fora do intervalo permitido!")
            except ValueError:
                print("Erro! Insira um valor numérico!")
        for v in valores [-10:]:
            print(f"\nValor: {v}")
            print(f"Primo: {primos(v)}")
            print(f"Divisores: {divisores(v)}")
            print(f"Perfeito: {perfeito(v)}")
            print(f"Par ou Impar: {par_impar(v)}")
        if len(valores) < 50:
            continuar = input("Deseja continuar? (S/N): ")
            if continuar == "S":
                continue
            elif continuar == "N":
                break

def calculadora():
   
    while True:
        try:
            print("\nO que vamos calcular?\n")
            print("1) Soma")
            print("2) Subtração")
            print("3) Multiplicação")
            print("4) Divisão")
            print("5) Voltar ao menu inicial")
            opt = int(input("Escolha uma operação: "))
            
            if opt == 5:
                print("Voltou ao menu principal!")
                break
            
            while True:
                    num1= int(input("Insira o 1º número: "))
                    if num1 < 1 or num1 > 1000:
                        print("Valor Inválido! Insira um número de 1 a 1000.")
                    else:
                        break
            while True:
                    num2 = int(input("Insira o 2º número: "))
                    if num2 < 1 or num2 > 1000:
                        print("Valor Inválido! Insira um número entre 1 a 1000.")
                    else:
                        break

            if opt == 1:
                print(f"Resultado: {num1} + {num2} = {num1+num2}")
            elif opt == 2:
                print(f"Resultado: {num1} - {num2} = {num1-num2}")
            elif opt == 3:
                print(f"Resultado: {num1} * {num2} = {num1*num2}")
            elif opt == 4:
                if num1 == 0 or num2 == 0:
                    print("Erro! Divisão por zero!")
                else:
                    print(f"Resultado: {num1} / {num2} = {num1/num2}")
            else:
                print("Opção Inválida! Escolha entre 1 e 5")
        except ValueError:
            print("Insira um número!")

def main():
    while True:
        try:        
            print("\n|----Exercício 1----|\n")
            print("   1) Ver Números")
            print("   2) Calculadora")
            print("   3) Sair\n")
            opt = int(input("Escolha a sua opção: "))

            if opt == 1:
                ver_numeros()
            elif opt == 2:
                calculadora()
            elif opt == 3:
                print("Programa Terminado.")
                break
            else:
                print("Opção Inválida. Insira um número de 1 a 3.")
        except ValueError:
            print("Insira um número.")

main()