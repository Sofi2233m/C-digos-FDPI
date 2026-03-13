#####CODIGO DE ARTICULOS##
venta = 0
iva = 0
print("Tipos de articulos -> 1 - Libro electronico $30000, 2 - Libro impreso $45000, 3 - Revista $8000")

art = int(input("Dígite el tipo de articulo: "))
if art < 1 or art > 3:
    print("El tipo de artículo no es válido")
else: 
    can = int(input("Dígite la cantidad que va a comprar: "))


    if art == 1:
        venta = can * 30000
    elif art == 2:
        venta = can * 45000
    else:
        venta = can * 8000
        
    iva = venta * 0.19
    print("Total a pagar:", venta)
    print("Costo IVA:", iva)

###DENTRO DEL ELSE PARA QUE SI PONE UNA CANTIDAD MENOR A UNO Y MAYOR A 3 NO DEBERÍA FUNCIONAR"