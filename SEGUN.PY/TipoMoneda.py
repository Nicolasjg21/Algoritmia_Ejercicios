# Nombre: Programa para definir segun su Pais que moneda usa.

# Entradas:
# Moneda = Definir cual es su nacionalidad.


# Salidas:
#   El usuario obtendra su moneda segun el Pais seleccionado en el menu.

# Proceso: Por medio del numero que digite el usuario, se le
# brindara la moneda usada en el Pais.

print(
    """
======== PAISES ========
1.Colombia.
2.Argentina.
3.Brazil.
4.Rusia.
5.Mexico.
======================
"""
)


Moneda = int(input("¿Cual es su nacionalidad?: "))
match Moneda:
    case 1:
        print("Su moneda es el Peso Colombiano")
    case 2:
        print("Su moneda es el Peso Argentino")
    case 3:
        print("Su moneda es el Real")
    case 4:
        print("Su moneda es el Rublo")
    case 5:
        print("Su moneda es el Peso Mexicano")
    case _:
        print("Su pais no hace parte del listado.")
