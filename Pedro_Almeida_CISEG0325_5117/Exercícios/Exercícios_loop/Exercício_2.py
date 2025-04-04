for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))
    
    if numero % 2 == 0:
        print(f"{numero} é PAR.")
    else:
        print(f"{numero} é ÍMPAR.")