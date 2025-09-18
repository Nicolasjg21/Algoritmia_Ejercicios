# Nombre: Programa para seleccionar un dia de la semana y conocer su descuento.

# Entradas:
# DiaDesc = Variable reservada para realizar selecciones de los dias de la semana

# Salidas:
#   Confirmacion de descuento: La persona sabra que descuento tiene sgun el dia seleccionado"

# Proceso: Por medio del numero que digite (1-3) el usuario, conocera que porcentaje de descuento fue asignado al numero digitado.

DiaDesc = int(
    input(
        "Ingrese un numero del 1 al 7 para coonocer el descuento del dia seleccionado: "
    )
)
match DiaDesc:
    case 1:
        print("Lunes: 25% de descuento")
    case 2:
        print("Martes: 2% de descuento")
    case 3:
        print(" Miercoles: 9% de descuento ")
    case 4:
        print("Jueves: 7% de descuento")
    case 5:
        print("Viernes: 5% de descuento")
    case 6:
        print("Sabado: 15% de descuento")
    case _:
        print("Su numero digitado no se encuentra en las categorias de los prductos.")

if DiaDesc == 7:
    print("El dia domingo no hay descuento")
