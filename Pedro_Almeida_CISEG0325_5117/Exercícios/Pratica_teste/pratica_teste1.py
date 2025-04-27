lista=[]
nova_lista=[]

contador = 0



print(lista)


def inserir():
    global contador
    while contador < 5:
        num = (int(input("Insira os números na lista: ")))
        lista.append(num)
        contador += 1 

def multiplicar():

    nova_lista = []

    print(f"Lista Original: {lista}")

    for i in lista:
        nova_lista.append(i * 2)

    print(f"Nova lista multiplicada: {nova_lista}")

    return nova_lista


def verificar_par():
    pares=[]
    impares=[]
    for j in lista:
        if j %2 == 0:
            pares.append(j)
        else:
            impares.append(j)
    if pares:
        print(f"Números pares na lista: {pares}")
    if impares:
        print(f"Números impares na lista: {impares}")


def main():
    while True:
        print("\n Menú Principal")
        print("1) Inserir números na lista ")
        print("2) Multiplicar números na lista ")
        print("3) Encontrar Pares na lista")
        print("4) Terminar Programa")

        try:
            opt = int(input(f"Escolha uma opção: "))
            if opt == 1:
                inserir()
            elif opt == 2:
                multiplicar()
            elif opt == 3:
                verificar_par()
            elif opt == 4:
                print("Programa Terminado")
                break
            else:
                print("Opção Inválida.")
        except ValueError:
            print("Por favor, Insira um número.")

main()