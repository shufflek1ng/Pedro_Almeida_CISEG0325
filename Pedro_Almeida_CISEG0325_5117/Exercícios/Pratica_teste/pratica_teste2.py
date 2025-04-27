lista=[]
contador = 0

def inserir():
    global contador
    while contador < 10:
        num=int(input("Insira os números na lista:"))
        lista.append(num)
        contador += 1

def ordenar():
    if lista:
        lista.sort()
        print(f"Lista Ordenada: {lista}")
    else:
        print("A lista está vazia!\n")

def classificar():
    if lista:
        positivos=[]
        negativos=[]

        for i in lista:
            if i < 0:
                negativos.append(i)
            
            else:
                positivos.append(i)

        print(f"Positivos: {positivos}")        
        print(f"Negativos: {negativos}")
    else:
        print("A lista está vazia!\n")

def somar():
    if lista:

        total = sum(lista)
        print(f"Soma de todos os números na lista: {total}")
    else:
        print("A lista está vazia!\n")

def ver():
    if lista:
        print(f"Lista: {lista}")
    else:
        print("A lista está vazia!\n")

def menu():

    while True:
        try:
            print("Menu Principal\n ")
            print("1) Inserir números: ")
            print("2) Ver Lista: ")
            print("3) Ordenar números: ")
            print("4) Classificar números ( Positivos / Negativos ): ")
            print("5) Somar números: ")
            print("6) Sair do Programa.")
            opt = int(input("Escolha uma opção: "))
            if opt == 1:
                inserir()
            elif opt == 2:
                ver()
            elif opt == 3:
                ordenar()
            elif opt == 4:
                classificar()
            elif opt == 5:
                somar()
            elif opt == 6:
                print("Saída com sucesso.")
                break
            else:
                print("Opção não existe, tente novamente.")
        except ValueError:
            print("Valor Inválido, insira um número por favor.")

menu()
    