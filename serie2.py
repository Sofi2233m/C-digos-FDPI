###Serie distinta 1/i


def serie():
    suma = 0

    for i in range(1,11):
        suma += 1/i
    return suma
    
print("Resultado: ", serie())


#serie 2/i^2
def serie():
    suma = 0

    for i in range(1,21):
        suma += 2/(pow(i,2))
    return suma
    
print("Resultado: ", serie())