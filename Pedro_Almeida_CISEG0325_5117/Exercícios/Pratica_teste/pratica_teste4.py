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
        ano=int(input("Digite o ano do livro: "))
        titulos.append(titulo)
        autores.append(autor)
        anos.append(ano)

def listar():
    for i in range(len(titulos)):
        print(f"{titulos}, de {autores}, {anos} na posição {i+1}")

def procurar():
    pass

def apagar():
    pass

 





def main():
    print("\n                                                                              |||Sistema de gestão de Livros|||\n")
    
    while True:

        try:
            print("----Menu Principal----\n")
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