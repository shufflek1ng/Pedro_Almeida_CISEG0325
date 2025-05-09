import time

class Carro:
    def __init__(self, marca, modelo, ano, vel):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.vel = vel

    def Acelera(self, nivel):
        if nivel == 1:
            self.vel += 10
        if nivel == 2:
            self.vel += 15
        if nivel == 3:
            self.vel += 20

    def Trava(self, nivel):
        if nivel == 1:
            self.vel -= 10
        if nivel == 2:
            self.vel -= 15
        if nivel == 3:
            self.vel -= 20

time.sleep(1)

Carro1 = Carro("BMW","M3","2020",0)
print("Velocidade do carro: ", Carro1.vel)
Carro1.Acelera(1)
time.sleep(1)
print("Velocidade do carro: ", Carro1.vel)
Carro1.Acelera(2)
time.sleep(1)
print("Velocidade do carro: ", Carro1.vel)
Carro1.Acelera(3)
time.sleep(1)
print("Velocidade do carro: ", Carro1.vel)
Carro1.Trava(3)
time.sleep(1)
print("Velocidade do carro: ", Carro1.vel)
Carro1.Trava(2)
time.sleep(1)
print("Velocidade do carro: ", Carro1.vel)
Carro1.Trava(1)
time.sleep(1)
print("Velocidade do carro: ", Carro1.vel)
Carro1.Acelera(3)
time.sleep(1)
print("Velocidade do carro: ", Carro1.vel)
Carro1.Acelera(2)
time.sleep(1)
print("Velocidade do carro: ", Carro1.vel)
Carro1.Acelera(1)
time.sleep(1)
print("Velocidade do carro: ", Carro1.vel)