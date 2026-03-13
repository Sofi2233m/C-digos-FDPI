####FUNCIONES####
#PSEUDOCODIGO

def calcular_iva(venta):

    iva = venta * 0.19
    
    return iva

venta = 0

print("Digite la venta: ")

venta = int(input())
print(calcular_iva(venta))
    