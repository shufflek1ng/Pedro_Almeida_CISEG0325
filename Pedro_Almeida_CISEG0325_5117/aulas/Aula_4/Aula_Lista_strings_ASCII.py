import time
# Controlo de listas em 2 dimensões
cidades = [ "Lisboa", "Madrid", "São Paulo" ]

#print(cidades[0][5])
#print(ord(cidades[0][5]))

#Index de 1ª Dimensão (palavra)  0  ,  1  ,  2
i=0
it=0
while i<=2:
    print(f"1ªDimensão i = {i}") #numeros[i][?]
    print(f"Valor na 1ª Dimensão :" cidades[i])
    time.sleep(1)
