peso=input("¿Cuál es el peso? (kilogramos) ")
estatura=input("¿Cuál es la estatura? (metros) ")
imc=round((int(peso))/((float(estatura))**2),2)
print ("El valor del IMC es: "+str(imc))
