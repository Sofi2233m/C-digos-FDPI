###CANTIDAD DE PARES E IMPARES##

def par(num):
    if num % 2 == 0:
        return True
    else: 
        return False
    
pares = 0
impares = 0

for i in range(1,6):
    num = int(input("Ingrese un número: "))
    
    if par(num):
        pares += 1
    else:
        impares += 1
        
print("Pares: ", pares)
print("Impares: ", impares)