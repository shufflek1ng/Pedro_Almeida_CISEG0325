marcas = []
modelos = []

contador_marca = 1
contador_modelo = 1

def listar():
    print("\nLista e respectivas posições:")
    for i in range(len(marcas)) or i in range(len(modelos)):
        print(f"{i+1}. {marcas[i]} {modelos[i]}")
    input("\nPressione Enter para voltar ao menu...")
    main()
        


def inserir():
    while len(marcas) < 2 and len(modelos) < 2:
        marca = input("Insira a marca do veiculo que pretende adicionar: ")
        if marca == 'sair':
            print("Voltou ao Menu!")
            break
        modelo = input("Insira o modelo do veículo que pretende adicionar: ")
        if modelo == 'sair':
            print("Voltou ao Menu!")
            break
        marcas.append(marca)
        modelos.append(modelo)
    else:
        print("\nLista Cheia!")
        input("\nPressione Enter para voltar ao menu...")
        main()


def procurar():
    if not marcas and not modelos:
        print("As listas estão vazias!\n")
        return

    procura=input("\nInsira a marca ou modelo que deseja encontrar: ")
    encontrado = False

    for i in range(len(marcas)) or i in range(len(modelos)):
        if procura == marcas[i] or procura == modelos[i]: 
            print(f"\nVeículo encontrado  na posição {i+1}: {marcas[i]} {modelos[i]}")
            encontrado = True

    if not encontrado:
        print(f"\n{procura} não foi encontrado na lista.")
    
    input("\nPressione Enter para voltar ao menu...")
    main()    

def apagar():
    if not marcas or not modelos:
        print("As listas estão vazias\n")
        return
    try:
        pos= int(input("Insira a posição que pretende eliminar: "))

        if 1 <= pos <= len(marcas):
            print(f"Veículo eliminado: '{marcas[pos-1]} {modelos[pos-1]}' da posição ({pos})")
        else:
            print("Posição Inválida ou inexistente!")
    except ValueError:
        print("ERRO! Insira um número! ")


def main():
    while True:
        try:
            print("\n Menu Principal\n")
            print(" 1) Introduzir Veículos")
            print(" 2) Procurar Veículos")
            print(" 3) Apagar Veículos")
            print(" 4) Listar Todos os veículos")
            print(" 5) Sair\n")

            opt= int(input("Escolha uma Opção: "))

            if opt == 1:
                inserir()
            elif opt == 2:
                procurar()
            elif opt == 3:
                apagar()
            elif opt == 4:
                listar()
            elif opt == 5:
                print("Programa Terminado")
                break
            else:
                print("Opção Inválida")
        except ValueError:
            print("Erro! Digite um número inteiro!")
main()