import time

hora = int(time.strftime('%H'))
minutos = int(time.strftime('%M'))

print("Son las ",hora,":",minutos,"HRS")

if hora >= 19:
    print("Es hora de ir a casa")
else:
    horaRestante=18-hora
    minutosRestantes=59-minutos
    print("Quedan",horaRestante,"horas y",minutosRestantes,"minutos para ir a casa")
