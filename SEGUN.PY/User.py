# Nombre: Programa para seleccionar un usuario de una corporacion.

# Entradas:
# User: Variable hecha para almacenar el usuario que se le asigne a el usuario.

# Salidas:
#   Confirmacion de usuario: Al final el usuario sabra que puesto le fue asignado.

# Proceso: Por medio del numero que digite (1-4) el usuario sera asigando a su respectivo rol.

User = int(input("Digite un numero del 1 al 4 para conocer su usuario: "))
match User:
    case 1:
        print("Admin")
    case 2:
        print("Invitado")
    case 3:
        print("Cliente")
    case 4:
        print("vendedor")
    case _:
        print("Su numero digitado no se encuentra en la lsiat de usuarios.")
