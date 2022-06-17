
def Menu():
    print("\n")
    print("<---- Menu de opciones ---->")
    print("(1) \tCrear Directorio")
    print("(2) \tAñadir Contacto")
    print("(3) \tBuscar")
    print("(4) \tOpciones de Contacto (NO implementado)")
    print("(5) \tListar directorio")
    print("(0) \tSalir")
    print("\n")
    opcion=input("¿Cuál es tu elección? ---->  ")
    return int(opcion)

def subMenuBuscar():
    print("\n")
    print("<---- Buscar Contacto ---->")
    print("(1) \tBusqueda por nombre")
    print("(2) \tBusqueda por telefono (NO implementado)")
    print("(0) \tRegresar")
    print("\n")
    opcion=input("¿Cuál es tu elección? ---->  ")
    return int(opcion)

def subMenuEditar():
    print("\n")
    print("<---- Editar Contacto ---->")
    print("(1) \tEditar contacto (NO implementado)")
    print("(2) \tEliminar contacto (NO implementado)")
    print("(0) \tRegresar")
    print("\n")
    opcion=input("¿Cuál es tu elección? ---->  ")
    return int(opcion)

def agregarContacto():
    print("<---- Añadir Contacto ---->")
    nombre=None
    while nombre==None:
        nombre=input('Nombre -->  ')
    telefono=None
    while telefono==None:
        telefono=input('Telefono -->  ')
    telefonos[nombre]=telefono
    nombres[telefono]=nombre
    return [nombre,telefono]

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

nombreDirectorio=None
directorio=[]
nombres={}
telefonos={}

sel=1
while sel!=0: 

    sel=Menu()

    if (sel>6):
        continue

    if sel == 1:
        nombreDirectorio=input('Indica el nombre del directorio -->  ')
        nombreDirectorio=nombreDirectorio+'.txt'
        continue
    elif sel == 2:
        datos=agregarContacto()
        directorio.append(datos)
        if nombreDirectorio:
            escribe(nombreDirectorio,datos)
        else:
            nombreDirectorio='default.txt'
            creaArchivo(nombreDirectorio)
            escribe(nombreDirectorio,datos)
        continue
    elif sel == 3:
        sel2=1
        while sel2!=0:
            sel2=subMenuBuscar()
            if sel2>3:
                continue
            if sel2==1:
                bnombre=input('Introduce el nombre -->  ')
                info=leer(nombreDirectorio)
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
                    print('<---- Cadena encontrada ---->')
                    print('Numero de coincidencias',cPalabra)
                for i in ListaNombre:
                    print('Nombre: ',i[0],'\tTelefono: ',i[1])
                if bandera!=1:
                    print('X---- Contacto no encontrada ----X')
            elif sel2==2:
                btelefono=input('Introduce el telefono -->  ')
                info=leer(nombreDirectorio)
                for e in info:
                    contacto=e.split(',')
                    if btelefono==contacto[1]:
                        print("Nombre: ",contacto[0],"\tTelefono:",contacto[1])
                        break
                                            
            else:
                break

    elif sel == 14: ## cambiar a 4 cuando se implementen las opciones de contacto
        sel3=1
        while sel3!=0:
            sel3=subMenuEditar()
            if sel3==2:
                enombre=input('Introduce el nombre a borrar -->  ')
                indice=None
                for i in range(len(directorio)):
                    if directorio[i][0]==enombre:
                        indice=i
                        break        
                if indice!=None:
                    del directorio[indice]
                    print(enombre,' BORRADO')
                else:
                    print(enombre,' NO ENCONTRADO')
            elif sel3==1:
                enombre=input('Introduce el nombre a editar -->  ')
                indice=None
                for i in range(len(directorio)):
                    if directorio[i][0]==enombre:
                        indice=i
                        break
                if indice != None:
                    print ('Deja en blanco los campos que deseas conservar')
                    nombre3=input('Nombre -->  ')
                    telefono3=input('Telefono -->  ')
                    directorio[indice]=[ nombre3 if len(nombre3)>0 else directorio[indice][0],
                    telefono3 if len(telefono3)>0 else directorio[indice][1]
                    ]
                    print('EDICION EXITOSA')
                else:
                    print('Contacto no encontrado')
            else:
                break
               
        else:
            break
    elif sel==5:
        if nombreDirectorio:
            print ("<---- Lista: ",nombreDirectorio," ---->")
        else:
            print ("<---- Lista ---->")
        info=leer(nombreDirectorio)
        for e in info:
            contacto=e.split(',')
            print("Nombre: ",contacto[0],"\tTelefono:",contacto[1])
    else:
        print("Gracias por utilizar el programa")