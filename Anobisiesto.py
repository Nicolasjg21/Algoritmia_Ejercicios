# Nombre: Programa para comprobar si el año es bisiesto o no.

# Entradas:
#   Año: Año que decice escoger el usuario para comrpobarlo.

# Salidas:
#   Confirmacion de año: Comprueba si el año es bisiesto o no.

# Proceso: Por medio del año que ponga el usuario, el sistema decide y calcula si el año ingresado oes bisiesto o no

Año = int(input("Ingrese el año: "))
if Año % 4 == 0 and Año % 100 != 0 or (Año % 400 == 0):
    print("El año es bisisesto")
else:
    print("El año no es bisiesto")
