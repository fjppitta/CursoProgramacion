entradaOriginal=input("\n\nDame la lista de paises\n-->  ")
entradaMinus=entradaOriginal.lower()

lista=list(set(entradaMinus.split(',')))

lista.sort()
listaTexto=",".join(lista)
salida=listaTexto.title()
print('\nLista Ordenada\n')
print(salida)
print('\n')



## Entrada:
## Canada,Estados Unidos,Mexico,Turquia,Rumania,Grecia,Italia,Panama,Bolivia,Peru,Chile,Brazil,Uruguay,Argentina,Bahamas,Venezuela,Mexico,Panama,Guatemala,Chile,Brazil,Uruguay,Argentina,Egipto,Arabia Saudita,grecia,italia,panama,GuaTEmala,Bolivia