

def caracter(vara):
    if "a" >= vara and vara <= "m" or "A" >= vara and vara <= "M": ####MAYÚSCULAS Y MINÚSCULAS####

        return 0
    elif vara >= "n" and vara <= "z" or "N" >= vara and vara <= "Z":
        return 1

letra = str(input("Escriba una letra del alfabeto: "))

print("Resultado:", caracter(letra))


