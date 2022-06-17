class Vehiculo():
    def __init__(self,color,ruedas,puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas
## Fin de la clase
        
class Coche(Vehiculo):
    def __init__(self,color,ruedas,puertas,velocidad,cilindrada):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas
        self.velocidad=velocidad
        self.cilindrada=cilindrada
## Fin de la clase

sedan=Coche("verde",4,5,120,200)

print("Tienes un coche color",sedan.color, "el cual tiene",sedan.ruedas,"ruedas y",sedan.puertas,"puertas.")
print("La velocidad máxima es de",sedan.velocidad,"km/h y una cilindrada de",sedan.cilindrada,"cc.")

