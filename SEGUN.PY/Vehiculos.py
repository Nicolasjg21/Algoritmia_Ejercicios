# Nombre: Programa para seleccionar una seccion de vehiculos segun el # de llantas.

# Entradas:
# vehiculos: Variable hecha pa almacenar el numero de neumaticos que digite el usuario.

# Salidas:
#   Confirmacion de vehiculo: Mostrar la seccion segun el # de llantas.

# Proceso: Por medio del numero que digite (2-4), el usuario obtendra una seccion de vehiculos.

vehiculos = int(input("Digite del 2 al 4 el numero de nehumaticos de su vehivulo "))
match vehiculos:
    case 2:
        print("Moto, Bicileta, Mono Patin")
    case 3:
        print("Tuc Tuc, Bici Taxi")
    case 4:
        print("Automovil, Cuatrimoto")
    case _:
        print("Su vehiculo no esta dentro de las secciones.")
