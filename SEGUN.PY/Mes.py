# Nombre: Programa para seleccionar un mes del año.

# Entradas:
# option: Variable hecha pa almacenar el numero seleccionado.

# Salidas:
#   Mes seleccionado: segun el numero seleccionado por el usuario se mostrara el mes respectivo.

# Proceso: Por medio del numero que digite  el usuario (1-12), se presentara el mes que se le asigno al numero.

option = int(input("Ingrese un numero del 1 al 12 para hallar el mes: "))
match option:
    case 1:
        print("Enero")
    case 2:
        print("Febreo")
    case 3:
        print("Marzo")
    case 4:
        print("Abril")
    case 5:
        print("Mayo")
    case 6:
        print("Junio")
    case 7:
        print("Julio")
    case 8:
        print("Agosto")
    case 9:
        print("Septiembre")
    case 10:
        print("Octubre")
    case 11:
        print("Noviembre")
    case 12:
        print("Diciembre")
    case _:
        print("El numero ingresado no corresponde a un mes")
