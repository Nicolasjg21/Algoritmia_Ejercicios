# Nombre: Programa para seleccionar un tipo de material segun su codigo.

# Entradas:
# codigo: Variable hecha pa almacenar el numero de codificacion de un material que escoja el usuario.

# Salidas:
#   Confirmacion de material: Segun el codigo se mostrara el material asigndo al numero.

# Proceso: Por medio del codigo que digite, el usuario se le asiganra un material.

codigo = int(input("Digite el codigo respecto de su material: "))
match codigo:
    case 1234:
        print("Oro")
    case 4523:
        print("Plata")
    case 9876:
        print("Diamante")
    case 3435:
        print("Madera")
    case _:
        print("Su material no existe")
