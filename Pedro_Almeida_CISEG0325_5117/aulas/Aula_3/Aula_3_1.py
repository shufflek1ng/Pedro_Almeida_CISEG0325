#match case - compara a igualdade entre elementos

opt="0"

print("press RK - ROCK")
print("press PP - POP")
print("press JZ - JAZZ")

opt= input("Escolha uma opção: ")
match opt:
    case "RK":
        print("Ouvir Rock")
    case "PP":
        print("Ouvir Pop")
    case "JZ":
        print("Ouvir Jazz")
    case _:
        print("Opção inválida")