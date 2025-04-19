import time

numeros = [4,3,6,2,1,0]
troca = True
#Index 
#Length 6
i = 0

numaux = 0


while True:
    i=0
    print(f"variavel{i} Lista de números {numeros}")
    time.sleep(1)
    troca=False
    while i <= 4:
        if (numeros[i]>numeros[i+1]):
            numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
        print(i)
        print(f"variavel{i}")
        i+=1
print(f"Lista ordenada: {numeros}")