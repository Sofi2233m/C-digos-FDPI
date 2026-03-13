import math as m
num1 = float(input("Digite el primer número: "))
num2 = float(input("Digite el segundo número: "))


def suma(a,b):
    return a + b

print("Resultado suma: ", suma(num1,num2))


def resta(a,b):
    return a - b

print("Resultado resta: ", resta(num1,num2))

def div(a,b):
    if b == 0:
        return "El divisor no puede ser cero"
    else:
        return a / b

print("Resultado división: ", div(num1,num2))

def residuo(a,b):
    if b == 0:
        return "El divisor no puede ser cero"
    else:
        return a % b

print("Resultado residuo: ", residuo(num1,num2))

def raiz(a):
    if a < 0 :
        return "El número debe ser positivo"
    else:
        return m.sqrt(a)

print("Resultado raíz cuadrada #1: ", raiz(num1))

def raiz(b):
    if b < 0 :
        return "El número debe ser positivo"
    else:
        return m.sqrt(b)

print("Resultado raíz cuadrada #2: ", raiz(num2))

def potencia(a,b):
    if a < 0:
        return "La potencia no puede ser negativa"
    else:
         return pow(b,a)

print("Resultado potencia: ", potencia(num1, num2))
