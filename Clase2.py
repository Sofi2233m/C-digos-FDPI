#EJERCICIO NO.1
#inicio
#Variables

venta = 0
iva = 0.0

#Entradas 
print("Digite el valor de la venta: ")

venta = int(input())

#Procesos
iva = venta * 0.19

#Salidas
print("El Iva es: ",iva)

#fin

#EJERCICIO NO. 2
#METODOLOGÍA
"""PASO 1: Analizar el problema
Descripcion: Desarrollar un programa que permita convertir grados
Celsius a Fahrenheit.

entrada: celsius
salida: fahrenheit

PASO 2: pseudocodigo
Inicio
 celsius : decimal
 fahrenheit : decimal
 preguntar(celsius)
 fahrenheit = (9 / 5) * celsius + 32
 mostrar(fahrenheit)
Fin

PASO 3: prueba de escritorio

Celsius                Fahrenheit
20.0                    68.0
25.8                    78.44
32.3                    90.14

PASO 4: Codificar el algoritmo en python
"""

celsius = 0
fahrenheit = 0

#entradas
celsius = float(input("Digite los grados en Celsius: "))

#Procesos
fahrenheit = (9/5) * celsius + 32
#salidas
print("El valor en Fahrenheit es; ", round(fahrenheit,2))
