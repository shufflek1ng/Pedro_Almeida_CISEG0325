pessoas = []

continuar = True
while continuar:
    print("\nMenu:")
    print("1. Adicionar nome")
    print("2. Listar por primeiro nome")
    print("3. Listar por último nome")
    print("4. Remover por primeiro nome")
    print("5. Remover por último nome")
    print("6. Sair")

    opcao = input("Escolha: ")

    if opcao == '1':
        while True:
            primeiro = input("Primeiro nome: ")
            ultimo = input("Último nome: ")

            valido = True

            if len(primeiro) < 1 or len(ultimo) < 1:
                valido = False
            else:
                p0 = ord(primeiro[0])
                u0 = ord(ultimo[0])

                if not (65 <= p0 <= 90):
                    valido = False
                if not (65 <= u0 <= 90):
                    valido = False

                for c in primeiro[1:]:
                    o = ord(c)
                    if 65 <= o <= 90:
                        valido = False
                        break

                for c in ultimo[1:]:
                    o = ord(c)
                    if 65 <= o <= 90:
                        valido = False
                        break

            if valido:
                idade_str = input("Idade: ")
                idade_valida = True
                for ch in idade_str:
                    if not (48 <= ord(ch) <= 57):  # verifica se é dígito
                        idade_valida = False
                        break

                if idade_valida:
                    idade = 0
                    for ch in idade_str:
                        idade = idade * 10 + (ord(ch) - 48)

                    pessoa = {"primeiro": primeiro, "ultimo": ultimo, "idade": idade}
                    pessoas.append(pessoa)
                    break
                else:
                    print("Idade inválida. Apenas números são aceites.")
            else:
                print("Nome inválido. Exemplo correto: Timóteo Amaro")

    elif opcao == '2' or opcao == '3':
        chave = "primeiro" if opcao == '2' else "ultimo"

        # Bubble Sort manual com ord
        n = len(pessoas)
        for i in range(n):
            for j in range(0, n - i - 1):
                a = pessoas[j][chave]
                b = pessoas[j + 1][chave]
                menor = False
                for x in range(min(len(a), len(b))):
                    if ord(a[x]) < ord(b[x]):
                        menor = True
                        break
                    elif ord(a[x]) > ord(b[x]):
                        menor = False
                        break
                else:
                    if len(a) < len(b):
                        menor = True

                if not menor:
                    temp = pessoas[j]
                    pessoas[j] = pessoas[j + 1]
                    pessoas[j + 1] = temp

        for p in pessoas:
            print(p["primeiro"] + " " + p["ultimo"] + " - " + str(p["idade"]) + " anos")

    elif opcao == '4':
        nome = input("Digite o primeiro nome a remover: ")
        removido = False
        for p in pessoas:
            if p["primeiro"] == nome:
                pessoas.remove(p)
                print("Removido:", p["primeiro"], p["ultimo"])
                removido = True
                break
        if not removido:
            print("Nome não encontrado.")

    elif opcao == '5':
        nome = input("Digite o último nome a remover: ")
        removido = False
        for p in pessoas:
            if p["ultimo"] == nome:
                pessoas.remove(p)
                print("Removido:", p["primeiro"], p["ultimo"])
                removido = True
                break
        if not removido:
            print("Nome não encontrado.")

    elif opcao == '6':
        continuar = False
        print("Programa encerrado.")

    else:
        print("Opção inválida.")