def Primo(numero):
    i=1
    contador=0
    while i<=numero:
        if (numero%i)==0:
            contador+=1
        if (contador>3):
            break
        i+=1
    if (contador==2):
        return True
    else:
        return False
## Termina la funcion
    
while True:
    numero= int (input("Dame un numero entero positivo mayor a 1: "))
    if (numero>1):
        break
    
if (Primo(numero)):
    print("El numero ",numero," es primo")
else:
    print("El numero ",numero," NO es primo")
