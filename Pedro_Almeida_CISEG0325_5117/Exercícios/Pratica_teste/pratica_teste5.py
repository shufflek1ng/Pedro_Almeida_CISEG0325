numeros=[]

def ver_numeros():
    pass

def calculadora():
    pass

def primo(numeros):
    pass

def contar_divisores(numeros):
    pass





def main():
    while True:
        try:
            print("\nMenu Principal\n")
            print("1) Ver números")
            print("2) Calculadora")
            print("3) Sair do programa")
            opt == int(input("Escolha a opção pretendida: "))

            if opt == 1:
                ver_numeros()
            elif opt == 2:
                calculadora()
            elif  opt == 3:
                print("Saiu do programa.")
            else:
                print("Escolha uma opção válida.") 
        except ValueError:
                print("Erro! Digite um número!")



main()