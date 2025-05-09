'''
def introdnome(nom):
    global nome
    nome=nom

def mostrarnome():
    print("O seu nome é", nome)

introdnome(input("Introduza O seu nome: "))
mostrarnome()
'''

'''
class Print:
    def __init__(self):
        print("Olá mundo")


printavel=Print()
'''

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def renovaridade(self,idade):
        self.idade = idade
    

Pessoas=[]

for i in range(3):
    nom=input("Digite o seu nome: ")
    idad=input("Digite a sua idade: ")
    Pessoas.append(Pessoa(nom,idad))

    print(f"Nome: ", Pessoas[i].nome)
    print(f"Idade: ", Pessoas[i].idade)

    novaidad=input("Digite nova idade: ")

    Pessoas[i].renovaridade(novaidad)
    print(f"Nome: ", Pessoas[i].nome)
    print(f"Idade: ", Pessoas[i].idade)