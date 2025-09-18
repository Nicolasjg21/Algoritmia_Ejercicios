# Nombre: Programa para seleccionar un color primario segun el orden postulado.

# Entradas:
# color: Variable hecha pa almacenar el color que escoja el usuario.

# Salidas:
#   Seleccion De Un Color: Segun el numero digitado, al usuario le sera asignado un color primario.

# Proceso: Por medio del numero que digite (1-3), el usuario sera propietario de un color primario.

color = int(input("Ingrese in numero del 1 al 3 para seleccionar un color primario: "))
match color:
    case 1:
        print("Rojo")
    case 2:
        print("Amarillo")
    case 3:
        print("Azul")
    case 4:
        print("Su numero no hace parte de un color primario.")
