import tkinter

## Funciones de los botones
def Salir():
    window.quit()

window=tkinter.Tk()

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)

lista=['Argentina','Bermudas','Canada','Dinamarca','Egipto']
lista_items=tkinter.StringVar(value=lista)
listbox=tkinter.Listbox(window,height=5,listvariable=lista_items)
listbox.grid(column=0,row=1,sticky='W')

etiqueta=tkinter.Label(window,text="Lista de Paises")
etiqueta.grid(column=0,row=0,sticky="W")

boton_salir=tkinter.Button(window,text='Salir',command=Salir)
boton_salir.grid(column=0,row=6,sticky="W")

window.mainloop()