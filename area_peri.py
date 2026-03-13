###CALCULAR AREA Y PERIMETRO###

def cal_area(alto1,ancho1):
    return alto * ancho

def cal_perim(alto,ancho):
    return (2 * alto) + (2 * ancho)

alto = float(input("Ingrese la altura del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))


print("Area: ", cal_area(alto, ancho))
print("Perímetro: ", cal_perim(alto, ancho))