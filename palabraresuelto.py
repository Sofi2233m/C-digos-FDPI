####BINARIO#3

def convertir(p):
    bin = ""
    for i in range(len(p)):
        if (p[i] >= "a" and p[i] <= "m") or (p[i] >= "A" and p[i] <= "M"):
            bin = bin + "0"
            
        else:
            bin = bin + "1"
    return bin

palabra = input("ingrese la palabra: ")
print("Resultado: ", convertir(palabra))


"""PSEUDOCODIGO
inicio funcion convertir(p)
    bin = texto
    para i en rango(tamano(p)):
        si (p[i] >= "a" and p[i] <= "m") or (p[i] >= "A" and p[i] <= "M"):
            bin = bin + "0"
            
        sino:
            bin = bin + "1"
        fin sí
    fin para
    retornar(bin)

fin funcion

inicio principal
    palabra: texto
    preguntar(palabra)
    mostrar(convertir(palabra))
fin
"""