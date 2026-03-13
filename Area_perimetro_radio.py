#METODOLOGÍA
"""PASO 1: Analizar el problema
Descripcion: Desarrollar un programa que permita calcular el área,
el perímetro y el diámetro de un círculo de radio r.

entrada: radio
salida: area, perimetro, diametro

PASO 2: pseudocodigo
Inicio
 radio, area, perimetro, diametro : decimal
 preguntar(radio)
 area = 3.14 * radio * radio
 perimetro = 2 * 3.14 * radio
 diametro = 2 * radio
 
 mostrar(area)
 mostrar(perimetro)
 mostrar(diametro)
Fin

PASO 3: prueba de escritorio

radio         area       perimetro      diametro
5             78.5       31.4           10.0
12            452.16     75.36          24.0
18            1017.36    113.4          36.0
 
PASO 4: Codificar el algoritmo en python
"""
#Inicio
#Variables

radio = 0
area = 0
perimetro = 0
diametro = 0

#entrada
radio = int(input("Digite el radio: "))

#Procesos
area = 3.14 * radio * radio
perimetro = 2 * 3.14 * radio
diametro = 2 * radio

#Salidas

print("Área", round(area,2))
print("Perímetro", round(perimetro,2))
print("Diámetro", round(diametro,2))



