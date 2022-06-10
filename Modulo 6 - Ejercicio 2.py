class Alumno():
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def mostrar(self):
        print ("Nombre: ",self.nombre)
        print ("Calificacion: ",self.nota)
    def esAprobado(self):
        if self.nota>=7:
            print("El alumno",self.nombre,"esta APROBADO")
        else:
            print("El alumno",self.nombre,"NO esta APROBADO")

## Fin de la clase

alumno1=Alumno()
alumno2=Alumno()
alumno3=Alumno()

alumno1.inicializar('Francisco',8)
alumno2.inicializar('Alberto',5)
alumno3.inicializar('Fatima',7)

alumno1.mostrar()
alumno2.mostrar()
alumno3.mostrar()

alumno1.esAprobado()
alumno2.esAprobado()
alumno3.esAprobado()
