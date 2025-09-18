# Nombre: Programa para seleccionar un dia de la semana y saber si es laboral o no.

# Entradas:
# Numeromes = Variable para seleccionar el dia de la semana.
# mensaje = Menu que contiene los dias de la semana.

# Salidas:
#   El usuario obtendra si el dia seleccionado es laboral o no.

# Proceso: Por medio del numero que digite el usuario, conocera si su dia es laboral o no.

mensaje = """
======== DIAS DE LA SEMANA ========
1.Lunes.
2.Martes.
3.Miercoles.
4.Jueves.
5.Viernes.
6.Sabado.
7.Domingo.
======================
"""
print(mensaje)

Numerolabo = int(
    input("""Seleccione un dia de la semana para definir si es laboral o no """)
)
match Numerolabo:
    case 1 | 2 | 3 | 4 | 5:
        print("Su dia es laboral")
    case 6 | 7:
        print("Su dia no es laboral")
