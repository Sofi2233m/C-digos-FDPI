###EDADES

edad = int(input("Ingrese su edad: "))

if edad >= 1 and edad <= 100:
    print("Es una edad válida")
    
elif edad >= 1 and edad <= 17:
    print("Usted es menor de edad")
    
elif edad >= 18 and edad <= 60:
    print("Usted es un adulto mayor")
    
elif edad >= 61 and edad <= 100:
    print("Usted es de la tercera edad")

else:
    print("No es una edad válida")


###Mejorando el Código

edad = int(input("Ingrese su edad: "))

if edad < 0 or edad > 100:
    print("NO es una edad válida")

elif edad < 18:
    print("Usted es menor de edad")
    
elif edad < 61:
    print("Usted es un adulto")
else:
    print("Usted es un adulto mayor" )
    
    
##O HACER IF ANIDADOS, DENTRO DEL ELSE 
