# Nombre: Programa para seleccionar un codigo para identificar el usuario.

# Entradas:
# User: Variable hecha para almacenar el codigo del usuario que se le asigno.

# Salidas:
#   Confirmacion de usuario: Al final, si el codigo esta bien, se dara la bienvenida.

# Proceso: Por medio del numero que digite el usuario sera aceptado o denegado.


User = int(input("Digite el codigo de su Rol: "))
match User:
    case 12536474:
        print("Admin, Bienvenido")
    case 24567:
        print("Invitado, Bienvenido")
    case 38765:
        print("Cliente, Bienvenido")
    case 41029:
        print("vendedor, Bienvenido")
    case _:
        print("Ust no hace parte de la empresa, DENEGADO.")
