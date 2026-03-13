#PINES VIRTUALES

#VARIABLES

npines = 0
total = 0
iva = 0
ganancia = 0

#entradas 
npines = int(input("Digite la cantidad de pines a comprar: "))

#PROCESOS
total = npines * 20000
iva = total * 0.19
ganancia = total - iva

#SALIDAS

print("DATOS DE LA VENTA")
print("Total a pagar: ", total)
print("IVA: ", iva)
print("Ganancia neta: ", ganancia)

#fin
