peso1=0.2
peso2=0.3
peso3=0.5

aluno=input("Digite o nome do aluno : ")
nota1=float(input("Digite o valor da 1ª Nota (0 a 10): "))
nota2=float(input("Digite o valor da 2ª Nota (0 a 10): "))              
nota3=float(input("Digite o valor da 3ª Nota (0 a 10): "))
        
media_final = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3)

print(f"Média Final: {media_final:.2f}")

if media_final >= 6:
    print(f"O aluno {aluno} está APROVADO com uma média final de {media_final:.2f}.")
else:
    print(f"O aluno {aluno} está REPROVADO com uma média final de {media_final:.2f}.")