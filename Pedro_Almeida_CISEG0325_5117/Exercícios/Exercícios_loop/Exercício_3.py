soma = 0

for i in range(1, 11):
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    soma += nota

media = soma / 10

print(f"\nA média das notas dos 10 alunos é: {media:.2f}")