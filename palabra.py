
def bina(p):
    resultado = ""
    
    for i in range(len(p)):
        if p[i] >= "a" and p[i] <= "m" or "A" >= p[i] and p[i] <= "M": ####MAYÚSCULAS Y MINÚSCULAS####
            resultado = resultado + "0"
        else:
            resultado = resultado + "1"

    return resultado

palabra = input("ingrese la palabra: ")
binario = bina(palabra)
print("Resultado: ", binario)