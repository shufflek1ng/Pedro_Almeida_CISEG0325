titulos=[]
autores=[]
anos=[]
contador = 1

def adicionar():
    while len(titulos) < 2 and len(autores) < 2 and len(anos) < 2:
        titulo=input("Escreva o título do Livro: ")
        if titulo == 'sair':
            print("Voltou ao menu.")
            break
        autor=input("Escreva o nome do autor: ")
        ano=input("Digite o ano do livro: ")
        titulos.append(titulo)
        autores.append(autor)
        anos.append(ano)

def listar():
    for i in range(len(titulos)):
        print(f"{titulos[i]}, de {autores[i]}, {anos[i]} na posição {i+1}")

def procurar():
    if not titulos and not autores and not anos:
        print("As listas estão vazias.\n")
        return
    
    termo = input("Insira o título do livro, autor ou ano que pretende procurar: ")

    encontrado = False

    for i in range(len(titulos)):
        if termo == titulos[i]:
            print(f"Livro encontrado na posição {i+1}: {titulos[i]} | Autor: {autores[i]} | Ano: {anos[i]}")
            encontrado = True

    for i in range(len(autores)):
        if termo == autores[i]:
            print(f"Livro encontrado na posição {i+1}: {autores[i]} | Titulo: {titulos[i]} | Ano: {anos[i]}")
            encontrado = True

    for i in range(len(anos)):
        if termo == anos[i]:
            print(f"Livro encontrado na posição {i+1}: {anos[i]} | Autor: {autores[i]} | Titulo: {titulos[i]}")
            encontrado = True
            
    if not encontrado:
        print(f"'{termo}' não foi encontrado nas listas.")


def apagar():
    if not titulos and not autores and not anos:
        print("As listas estão vazias! \n")
        return

    try:
        pos = int(input("Insira a posição do titulo que deseja eliminar na lista: \n"))

        if 1 <= pos <= len(titulos):
            print(f"Eliminado: Titulo: - ({titulos[pos-1]}) | Autor: - ({autores[pos-1]}) | Ano: - ({anos[pos-1]})")
            titulos.pop(pos-1)
            autores.pop(pos-1)
            anos.pop(pos-1)
        else:
            print("Posição não existe!")
    except ValueError:
        print("Por favor, insira um número válido.")



def main():
    print("\n                                                                              |||Sistema de gestão de Livros|||\n")
    
    while True:

        try:
            print("\n----Menu Principal----\n")
            print(" 1) Adicionar Livros: ")
            print(" 2) Listar Livros: ")
            print(" 3) Procurar Livros: ")
            print(" 4) Apagar Livro: ")
            print(" 5) Sair. \n")
            opt = int(input("Escolha uma das Opções: \n"))

            if opt == 1:
                adicionar()
            elif opt == 2:
                listar()
            elif opt == 3:
                procurar()
            elif opt == 4:
                apagar()
            elif opt == 5:
                break
            else:
                print("Opção Inválida! Essa opção não existe.")
        except ValueError:
            print("Erro: Insira um número.")

main()