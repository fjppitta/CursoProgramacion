import tkinter

window=tkinter.Tk()

## Funciones de los botones
def Reiniciar():
    variable.set(None)

def Salir():
    window.quit()

variable = tkinter.IntVar() 

runo = tkinter.Radiobutton(window, text='Lunes',variable=variable, value=1) 
rdos = tkinter.Radiobutton(window, text='Martes',variable=variable, value=2) 
rtres = tkinter.Radiobutton(window, text='Miercoles',variable=variable, value=3) 
rcuatro = tkinter.Radiobutton(window, text='Jueves',variable=variable, value=4) 
rcinco = tkinter.Radiobutton(window, text='Viernes',variable=variable, value=5) 
rseis = tkinter.Radiobutton(window, text='Sabado',variable=variable, value=6) 
rsiete = tkinter.Radiobutton(window, text='Domingo',variable=variable, value=7) 

runo.grid(column=0, row=0,sticky="W")
rdos.grid(column=0, row=1,sticky="W")
rtres.grid(column=0, row=2,sticky="W")
rcuatro.grid(column=0, row=3,sticky="W")
rcinco.grid(column=0, row=4,sticky="W")
rseis.grid(column=0, row=5,sticky="W")
rsiete.grid(column=0, row=6,sticky="W")

etiqueta=tkinter.Label(window,textvariable="Seleccion"+str(variable))
etiqueta.grid(column=1,row=8,sticky="W")

boton_reinicio=tkinter.Button(window,text='Reiniciar',command=Reiniciar)
boton_reinicio.grid(column=0,row=9,sticky="W")

boton_salir=tkinter.Button(window,text='Salir',command=Salir)
boton_salir.grid(column=2,row=9,sticky="E")


window.mainloop()
