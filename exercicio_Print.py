

print("\n")

nome = "Pedro Almeida"
idade = 31.5
cidade = "Setúbal"

print(f"Olá! O meu nome é {nome} ({type(nome)}). Eu tenho {idade} anos ({type(idade)}) e moro em {cidade} ({type(cidade)}).")

print("\n")

print("Exercício 2: Retângulo")

print("\n")

largura = 5
altura = 5

for i in range(altura):
    if i == 0 or i == altura - 1:
        print("X" * largura)
    else:
        print("X" + " " * (largura - 2) + "X")

print("\n")

print("Exercício 3: Pinheiro")

altura = 8

print("\n")


for i in range(altura):
    espacos = altura - i - 1
    asteriscos = i * 2 + 1
    print(" " * espacos + "X" * asteriscos)


for _ in range(2):
    print(" " * (altura - 2) + "XX")

print(" " * (altura -3) + "XXXX")