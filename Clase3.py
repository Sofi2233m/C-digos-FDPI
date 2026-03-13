##### IF ELSE ESTRUCTURAS DE DECISIÓN
##INICIO
##VARIABLES

edad = 0

##ENTRADAS

edad = int(input("Cuál es edad: "))

#PROCESOS
if edad < 18:
    #ENTRADA
    print("Usted es menor de edad")
else:
    #SALIDA
    print("Usted es mayor de edad")
#FIN


##ejercicio 2
#INICIO
x = 0 ##NO HAY NECESIDAD DE INCIALIZAR
f = 0 ## NO HAY NECESIDAD DE INICIALIZAR

x = int(input("Digite x: "))

if x > 0:
    f = 4 * pow(x,2) - 7
    print("f=", f)
else:
    f = -3 * x + 8
    print(" f= ", f)
    
    
##Para no repetir un print, se inicializa f arriba y se imprime fuera del if else   


###ELEVAR
print(pow(2,8))

##importar librerías

import math as m
print(m.sqrt(5))

