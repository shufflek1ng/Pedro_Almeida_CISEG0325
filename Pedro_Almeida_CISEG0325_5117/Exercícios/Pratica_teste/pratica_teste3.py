marcas=[]
modelos=[]

contador_marca = 1
contador_modelo = 1

def introduzir():
    while len(marcas) < 5 and len(modelos) < 5:
        marca = input("Insira a marca do carro ou digite 'sair' para voltar ao menu: ")
        if marca == 'sair':
            print("Voltou ao menu\n")
            break
        modelo = input("Insira o modelo do carro: ")
        marcas.append(marca)
        modelos.append(modelo)

def procurar():
    if not marcas and not modelos:
        print("As Listas estão vazias\n")
        return

    termo = input("insira a marca ou modelo que deseja encontrar: ")

    encontrado = False

    for i in range(len(marcas)):
        if termo == marcas[i]:
            print(f"Marca encontrada na posição {i+1}: {marcas[i]} - Modelo: {modelos[i]}")
            encontrado = True

            
    for i in range(len(modelos)):
        if termo == modelos[i]:
            print(f"Modelo encontrado na posição {i+1}: {modelos[i]} - Marca: {marcas[i]}")
            encontrado = True

    if not encontrado:
        print(f"'{termo}' não foi encontrado na lista.")

def eliminar():
    if not marcas or not modelos:
        print("As listas estão vazias!\n")
        return

    try:
        pos = int(input("Insira a posição que deseja eliminar (a partir de 1): "))

        if 1 <= pos <= len(marcas):
            print (f"Eliminado: Marca - ({marcas[pos-1]}) - Modelo - ({modelos[pos-1]}) da posição {pos}.")
            marcas.pop(pos-1)
            modelos.pop(pos-1)
        else:
            print("Posição Inválida. Insira uma posição existente: ")
    except ValueError:
        print("Por favor, insira um número válido.")


def main():

    while True:

        try:
            print("\n         --------MENU-------\n")
            print("         1) Introduzir Dados ")
            print("         2) Procurar Dados ")
            print("         3) Eliminar Dados ")
            print("         4) Sair \n")

            opt = int(input("Escolha uma opção: "))

            if opt == 1:
                introduzir()
            elif opt == 2:
                procurar()
            elif opt == 3:
                eliminar()
            elif opt == 4:
                print("Saiu com sucesso")
                break
            else:
                print("Opção não existe! Escolha uma opção de 1 a 4!")
        except ValueError:
            print("Erro. Escreva um número.")

main()
