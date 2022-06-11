def escribe(archivo,datos):
    f=open(archivo,'w')
    for linea in datos:
        if not linea.endswith('\n'):
            linea=linea+'\n'
        f.write(linea)
    f.close()
## Termina funcion para escribir archivo

def leer(archivo):
    f=open(archivo,'r')
    datos=f.readlines()
    f.close()
    return datos
## Termina funcion para leer archivo

lista = [
    'Francisco',
    'Juan',
    'Pedro',
    'Agustin',
    'Mario'
]

escribe('texto.txt',lista)
info=leer('texto.txt')

print(info)

