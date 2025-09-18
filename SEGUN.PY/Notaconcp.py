# Nombre: Programa para seleccionar un valor cualitativo a una nota.

# Entradas:
# nota: Variable hecha para escoger el rango donde se encuentra su nota.

# Salidas:
#   Seleccion de un valor cuanlitativo: Segun el numero digitado, al usuario le sera asignado un valor cualitativo con respecto a su rango numerico.

# Proceso: Por medio del numero que digite el usuario sera seleccionado en un rango donde se debe enontrar la nota obtenida,
# el usuario segun su rango tendra un valor cualitativo asignado.

print(
    """
================== NOTAS ==================
1. (0.0 - 3.9)
2. (4.0 - 5.9)
3. (6.0 - 7.0)
4. (7.1 - 8.4)
5. (8.5 - 9.4)
6. (9.5 - 10)
      """
)

nota = int(input("Ingrese su nota: "))
match nota:
    case 1:
        print("Su calificacion es extremadamente baja")
    case 2:
        print("Su calificacion es baja")
    case 3:
        print("Su calificacion es medianamente baja")
    case 4:
        print("Su calificacion es media")
    case 5:
        print("Su calificacion es medianamente alta")
    case 6:
        print("Su calificacion es extraordinaria")
