# Nombre: Programa para seleccionar un Pais y conocer cual es su lengua.

# Entradas:
# LenguaPais = variable para seleccionar el pais.


# Salidas:
#   El usuario obtendra la lengua natal del Pais seleccionado.

# Proceso: Por medio del numero que digite el usuario, se tendra en cuenta el pais seleccionado y
# se brindara el idioma natal de la opcion seleccionada.

print(
    """
======== PAISES ========
1.Colombia.
2.Estados Unidos.
3.Japon.
4.Brazil.
5.Australia.
======================
"""
)


LenguaPais = int(input("""Seleccione un Pais para comprobar que idioma hablan: """))
match LenguaPais:
    case 1:
        print("En Colimbia hablan español Latin")
    case 2:
        print("En E.E.U.U hablan Ingles")
    case 3:
        print("En Japon hablan Japones")
    case 4:
        print("En Brazil hablan Portugues")
    case 5:
        print("en Australia Hablan Ingles")
