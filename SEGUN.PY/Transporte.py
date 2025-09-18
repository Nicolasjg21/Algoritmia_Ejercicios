# Nombre: Programa para seleccionar un tipo de transporte por asignar.

# Entradas:
# Transporte: Variable hecha para almacenar el numero de vehiculo que fue asignado el user.
# Salidas:
#   Confirmacion de transporte, se mostrara que vehiculo le fue asignado a la persona.

# Proceso: Por medio del numero que digite el usuario (1-4) se presentara el tipo de transporte que se le asigno al numero.

tranporte = int(input("Ingrese un numero para conocer su tipo de transporte: "))
match tranporte:
    case 1:
        print("Automovil")
    case 2:
        print("Motocicleta")
    case 3:
        print("Bus")
    case 4:
        print("Taxi")
    case _:
        print("Su medioo de Transporte no existe aqui.")
