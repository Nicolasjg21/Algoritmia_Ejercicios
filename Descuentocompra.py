# Nombre: Programa para brindar descuento a una compra mayor de un monto.

# Entradas:
#   compra: Reconocer cual fue el monto de la compra del usuario.
#   descuento: Descuento a aplicar de la compra.

# Salidas:
#   Descuento aplicado o no: Segun el monto de la compra, se realiza despcuento o la compra queda con el mismo precio.

# Proceso: El usuario tiene que ingresar el monto de su compra, si su compra fue > 1000 entonces el decuento sera aplicado.

compra = float(input("Ingrese el monto de su compra: "))
if compra > 1000:
    descuento = compra * 0.10
    print("El descuento aplicado es: ", descuento)
else:
    print("Su descuento es 0")
