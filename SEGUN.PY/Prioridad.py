# Nombre: Programa para definir segun su edad que prioridad tiene.

# Entradas:
# edad = variable para obtener su edad segun el numero.


# Salidas:
#   El usuario obtendra su prioridad segun la edad seleccionada en el menu.

# Proceso: Por medio del numero que digite el usuario, tendra mas relevancia
# la prioridad o no.

print(
    """
==================== ¿QUE EDAD TIENE USTED? ====================
1. 1 año - 5 años.
2. 6 años - 14 años.
3. 15 años - 17 años.
4. 18 años - 59 años.
5. 60 años - ... años.
      """
)

edad = int(input("Segun el menu, que edad tiene usted?: "))
match edad:
    case 1:
        print("Usted tiene 100% de prioridad")
    case 2:
        print("Usted tiene 75% de prioridad")
    case 3:
        print("Usted tiene 50% de prioridad")
    case 4:
        print("Usted tiene 55-80% de prioridad")
    case 5:
        print("Usted tiene 100% de prioridad")
    case _:
        print("Usted no esta en el listado")
