import math

# Utilizando funciones con def

def AreaTriangulo(base,altura):
    return (base*altura)/2
## Fin de funcion

def AreaCirculo(radio):
    return round((math.pi*radio*radio),2)
## Fin de funcion

print("Triangulo")
base=int(input("Dame la base del triangulo: "))
altura=int(input("Dame la altura del triangulo: "))
print("Circulo")
radio=int(input("Dame el radio del circulo: "))

areaDeTriangulo=AreaTriangulo(base=base,altura=altura)
areaDeCirculo=AreaCirculo(radio=radio)
print("\nFunciones con def")
print("El area del triangulo es: ",areaDeTriangulo)
print("El área del circulo es: ",areaDeCirculo)


# Utilizando funciones anonimas (lambda)

ATriangulo = lambda base,altura: (base*altura)/2
ACirculo=lambda radio: round((math.pi*(radio*radio)),2)
print("\nFunciones anonimas (lambda)")
print("El area del triangulo es: ",ATriangulo(base=base,altura=altura))
print("El área del circulo es: ",ACirculo(radio=radio))
