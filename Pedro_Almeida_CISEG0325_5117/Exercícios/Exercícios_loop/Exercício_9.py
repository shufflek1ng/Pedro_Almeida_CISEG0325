while True:
    numero = int(input("Digite um número entre 1 e 100: "))
    
    if 1 <= numero <= 100:
        print(f"Obrigado! O número {numero} está dentro do intervalo.")
        break
    else:
        print("Número inválido. Tente novamente.")