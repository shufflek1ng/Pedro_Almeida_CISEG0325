horas = 0
minutos = 0
segundos = 0

tempo = int(input("Digite o tempo em segundos: "))

if tempo >= 3600:
    horas = tempo // 3600
    tempo = tempo % 3600

if tempo >= 60:
    minutos = tempo // 60
    tempo = tempo % 60

segundos = tempo

print(f"{horas} horas, {minutos} minutos e {segundos} segundos")