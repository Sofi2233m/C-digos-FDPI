import math as m


def cal_func(a,b): ###VARIABLES DISTINTAS LOCALES DE LA FUNCION###
    f = 3 * pow(a,2) + 2 * a * b - 7
    
    return f 


###FUNCIONES DEL PRGRAMA###
print("Dígite a:")
a = int(input())
print("Dígite b:")
b = int(input())

print(cal_func(a,b))
