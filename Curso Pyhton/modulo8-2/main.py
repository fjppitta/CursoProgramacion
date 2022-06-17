from pickle import *

class Vehiculo:
    def __init__(self,modelo,puertas):
        self.modelo=modelo
        self.puertas=puertas
    def __str__(self):
        return self.modelo+" "+self.puertas

carro=Vehiculo("Sedan","5")
print(carro)

f=open('binario','w+b')

dump(carro,f)
f.seek(0)
nuevoCarro=load(f)
print(nuevoCarro)
f.close()


