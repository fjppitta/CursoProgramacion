def creaArchivo(archivo):
    f=open(archivo,'w')
    linea='NOMBRE, TELEFONO\n'
    f.write(linea)
    f.close()

def escribe(archivo,datos):
    f=open(archivo,'a')
    linea=str(datos[0])+','+str(datos[1])+'\n'
    f.write(linea)
    f.close()

def leer(archivo):
    f=open(archivo,'r')
    datos=f.readlines()
    f.close()
    return datos

bnombre=input('Introduce el nombre -->  ')
info=leer('lista.txt')
nLinea=0
cPalabra=0
bandera=0
ListaNombre=[]
for e in info:
    nLinea+=1
    if bnombre in e.strip('\n'):
        bandera=1
        cPalabra+=1
        contacto=e.strip('\n')
        contacto=contacto.split(',')
        ListaNombre.append(contacto)
if bandera==1:
    print('Cadena encontrada')
    print('Numero de coincidencias',cPalabra)
    for i in ListaNombre:
        print('Nombre: ',i[0],'\tTelefono: ',i[1])
