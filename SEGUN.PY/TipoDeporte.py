# Nombre: Programa para seleccionar un tipo de deporte segun su numero de jugadores.

# Entradas:
# tdeporte: Variable hecha para almacenar el numero de jugadores de el deporte seleccionado.

# Salidas:
#   Confirmacion de su deporte(Probablemente): segun el numero de jugadores, el sistema puede llegar a identificar su deporte.

# Proceso: Por medio del numero de jugadores el sistema puede idetificar el deporte seleccionado.

tdeporte = int(input("¿Cuantos jugadores conforman su deporte?: "))
match tdeporte:
    case 5:
        print("Su deporte puede ser: Baloncesto, Futsal (microfútbol)")
    case 9:
        print("Su deporte puede ser: Béisbol")
    case 11:
        print("Su deporte puede ser: Fútbol(soccer), Críquet, Hockey sobre césped")
    case 2:
        print(
            "Su deporte puede ser: Tenis (dobles), Bádminton (dobles), Tenis de mesa (dobles"
        )
