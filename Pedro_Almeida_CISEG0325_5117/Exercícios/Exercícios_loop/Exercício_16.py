cont = 0
soma = 0

while cont < 30:
    num = int(input(f"Digite o {cont + 1}º número: "))
    
    if 1 <= num <= 50 and num % 2 == 0:
        soma += num
        cont += 1
    else:
        print("Número inválido! Só são aceitos pares entre 1 e 50.")

media = soma / 30
print(f"\nA média dos 30 números pares é: {media}")
