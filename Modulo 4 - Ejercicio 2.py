numeroInicial: int = int(input("Dame el número de inicio: "))
numeroFinal: int  = int(input("Dame el número final: "))

numerosImpares: [int] =[]

while numeroFinal <= numeroInicial:
    numeroFinal = int(input("El numero final debe ser mayor que el inicial. Vuelve a introducir el número: "))

for numero in range(numeroInicial, numeroFinal):
    if (numero%2 != 0):
        numerosImpares.append(numero)

print("La lista de número impares es:")
print(numerosImpares)
