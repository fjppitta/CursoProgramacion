def bisiesto(numero):
    division4=True if (numero%4)==0 else False
    division100=True if (numero%100)==0 else False
    division400=True if (numero%400)==0 else False
    if (division4 and (not division100 or division400)):
        return True
    else:
        return False
## Termina funcion
    
while True:
    numero=int(input("Dame un año (0 para salir): "))
    if numero<=0:
        break
    if (bisiesto(numero)):
        print("El año ES bisiesto")
    else:
        print("El año NO ES bisiesto")

print("Gracias por usar el programa")

