# Nombre: Programa para seleccionar un mes del año y saber en que estacion esta en el HM.

# Entradas:
# Numeromes = Variable para seleccionar el mes del año.
# mensaje = Menu para seleccionar el mes.

# Salidas:
#   El usuario obtendra la estacion por la cual pasa el mesdigitado.

# Proceso: Por medio del numero que digite el usuario, conocera la estacion actual de su mes.

mensaje = """
======== MESES DEL AÑO ========
1.Enero.
2.Febrero.
3.Marzo
4.Abril
5.Mayo.
6.Junio.
7.Julio.
8.Agosto.
9.Septiembre.
10.Octubre.
11.Noviembre.
12.Diciembre.
======================
"""
print(mensaje)

NumeroMes = int(
    input(
        """Seleccione un mes del año para 
definir su estacion en el hemisferio norte: """
    )
)
match NumeroMes:
    case 3 | 4 | 5:
        print("Su mes se encuentra en Primavera")
    case 6 | 7 | 8:
        print("Su mes se encuentra en Verano")
    case 9 | 10 | 11:
        print("Su mes se encuentra en Otoño")
    case 12 | 1 | 2:
        print("Su mes se encuentra en Invierno")
