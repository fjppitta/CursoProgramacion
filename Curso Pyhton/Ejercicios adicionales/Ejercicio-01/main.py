import os
import pprint
from tokenize import String
#from os import walk

def Menu():
    print("<---- Menu de opciones ---->")
    print("(1) Listar Archivos")
    print("(2) Listar Subdiretorios")
    print("(3) Listar Contenido de los subdirectorios")
    print("(0) Salir")
    print("\n")
    opcion=input("¿Cuál es tu elección? ---->  ")
    return opcion

def listadoArchivos(ruta='.'):
    return next(os.walk(ruta))[2]

def listadoSubdirs(ruta='.'):
    return next(os.walk(ruta))[1]

def ListaTodo(ruta = os.getcwd()):
    lista = []
    for archivos in os.walk(ruta):
        lista.extend(archivos)
    return lista

directorio_curso=r'C:\Users\fjppi\Documents\curso python'

if os.path.exists(directorio_curso):
    os.chdir(directorio_curso)
    lArchivos=listadoArchivos()
    lSubdirs=listadoSubdirs()
    Todo = ListaTodo()
else:
    print('El directorio no existe')

sel=1
while sel!=0: 

    sel=int(Menu())

    if (sel>3):
        continue

    if sel == 1:
        print('\nListado de Archivos')
        for arch in lArchivos:
            t=str(round(os.path.getsize(arch)/1024,2))
            print("{:<30} {:>10} KB".format(arch,t))
    elif sel == 2:
        print('\nListado de subdirectorios')
        for sdir in lSubdirs:
            print(sdir)
    elif sel == 3:
        print('\nListado de todo')
        for todo in ListaTodo(directorio_curso):
            print(todo)
    else:
        print("Gracias por utilizar el programa")
    
    print('\n')