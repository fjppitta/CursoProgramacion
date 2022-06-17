from functools import reduce

def ObtenerImpares(lista): 
    impares = list(filter((lambda x: x % 2), lista)) 
    suma = reduce( (lambda x, y: x + y), impares) 
    print('Lista de Impares:\n',impares,'\n')
    print('La suma de los Impares da: ',suma)

lista = list(range(200))

print('\n')
ObtenerImpares(lista)
print('\n')