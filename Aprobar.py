#INICIO
#METODOLOGÍA
"""
nombre: Sofía Montealegre Polanco
correo: sofia.montealegre@correounivale.edu.co


PASO 1: Analizar el problema
Descripcion: Para aprobar un curso, es necesario obtener un
promedio mínimo de 3.0 en tres actividades. Diseñe un programa
que solicite las calificaciones de las dos primeras actividades y
calcule la nota necesaria en la tercera para alcanzar al menos un
promedio de 3.0 como calificación final.

entrada: cal1, cal2, promedio
salida: cal3

PASO 2: pseudocodigo
Inicio
cal1, cal2, cal3, prom: decimal
preguntar(cal1)
preguntar(cal2)

prom = (cal1 + cal2 + cal3)/3.0

cal3 = 3.0 * prom * (cal1 -cal2)

mostrar(cal1)
mostrar(cal2)
mostrar(cal3)
Fin

PASO 3: prueba de escritorio

calificacion1          calificacion2       calificacion
3.5                       4.0                1.5
               
                   
                  

PASO 4: Codificar el algoritmo en python
"""
#VARIABLES
cal1 = 0
cal2 = 0
cal3 = 0

prom = 9.0

#ENTRADA
cal1 = float(input("Digite la calificacion 1: "))
cal2 = float(input("Digite la calificacion 2: "))


#SALIDA

cal3 = prom -cal1-cal2

print("Calificacion 1: ", cal1)
print("Calificaion 2: ", cal2)
print("Calificacion 3: ", cal3)

#FIN