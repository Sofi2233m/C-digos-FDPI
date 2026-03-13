##IMPRIMA LA SUMATORIA DE LOS 5 PRIMEROS NUMEROS###
inicio = int(input("Ingrese el número incial: "))
fin = int(input("Ingrese el número final: "))
paso = int(input("Ingrese el número de paso: "))

suma = 0
for i in range(inicio, fin, paso):
    suma = suma + i
    
print("Resultado: ", suma)


####Más corto##

n = int(input("Ingrese hasta que número sumar: "))
suma = 0
for i in range(1, n+1, 1):
    suma = suma + i
    
print("Resultado: ", suma)

####CON FUNCIONES###

def sumatoria(num):
    sum = 0
    for i in range(1, num+1):
        sum += i ##igual que sum = sum + i 
    return sum

n = int(input("Ingrese un número: "))
print("Sumatoria de", n, ":", sumatoria(n))


"""
PSEUDOCODIGO

inicio funcion sumatoria(num)
    sum: entero
    para i en rango(1,num+1)
        sum = sum + i 
    fin para
    retornar (sum)
fin funcion

inicio principal
    n: entero
    preguntar(n)
    mostrar(sumatoria(n))
fin
"""