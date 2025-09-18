# Nombre: Programa para seleccionar un usuario de una corporacion.

# Entradas:
# User: Variable hecha para almacenar el usuario que se le asigne a el usuario.

# Salidas:
#   Confirmacion de usuario: Al final el usuario sabra que puesto le fue asignado.

# Proceso: Por medio del numero que digite (1-4) el usuario sera asigando a su respectivo rol.

profesion = int(input("Digite su codigo reservado para conocer su profesion: "))
match profesion:
    case 1234:
        print("Ingeniero")
    case 5647:
        print("Policia")
    case 6789:
        print("Profesor")
    case 5346:
        print("Enfermero")
    case _:
        print("Su numero digitado no se encuentra en la lsiat de profesiones.")
