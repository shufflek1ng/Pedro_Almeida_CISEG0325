import time
# Algoritmo para procura
nomproc=""
contaigualdade=0
#index i      0               1                2               3
nomes=["Dario Quental", "Joao Matos", "Liliana Queiroz", "Joao Matos"]
indes_proc=[]
#       0123456789101112
#Nomes[i][it]
'''
nomproc="Joao Matos"  #nome que procuro
#        0123456789

#for nome in Nomes: #for vai precorrer todos os nomes da lista
#    print(nome[0]) #imprime a 1ª letra de cada  nome

for i in range(len(nomes)): #for vai precorrer todos os nomes da lista
    print(f"valor de i no for externo:", i)
    for it in range(len(nomes[i])):
        time.sleep(1)
        print(f"valor de it no for interno:", it)
        print(nomes[i][it]) #imprime Cada string na lista associado a um valor que está representado na linha anterior
        print(nomproc[it])
        if it== (len(nomproc)-1):
            print("tamanho do valor dentro de nomproc: ",len(nomproc))
            break
'''
nomproc="Joao Matos Pereira"  #nome que procuro
#        0123456789

#for nome in Nomes: #for vai precorrer todos os nomes da lista
#    print(nome[0]) #imprime a 1ª letra de cada  nome

for i in range(len(nomes)): #for vai precorrer todos os nomes da lista
    print("valor de i no for externo roda 1ª dimensão da lista: ", i)
    contaigualdade=0
    print("Nome no index 1ª Dimensão: ",nomes[i])
    for it in range(len(nomes[i])):
        time.sleep(1)
        print("valor de it no for interno roda 2ª Dimensão da lista: ", it)
        print(nomes[i][it]) #imprime Cada string na lista associado a um valor que está representado na linha anterior
        print(nomproc[it])
        if ord(nomes[i][it]) == ord(nomproc[it]): #transforma os nomes em números
            contaigualdade+=1
        print("Igualdade: ", contaigualdade)
        if contaigualdade == len(nomproc):
            print("Nome em nomes" ,nomes[i],"posição da lista:", i)
            print("nome em nomproc: ", nomproc)
        if it== (len(nomproc)-1):
            print("tamanho do valor dentro de nomproc: ",len(nomproc))
            break