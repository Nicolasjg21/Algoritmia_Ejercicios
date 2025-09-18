# Nombre: Programa para definir su categoria segun su edad .

# Entradas:
# edad = variable para obtener su edad segun el numero.


# Salidas:
#   El usuario obtendra su categoria segun la edad seleccionada en el menu.

# Proceso: Por medio del numero que digite el usuario, obtendra su categoria.

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
        print("Usted es un bebe")
    case 2:
        print("Usted es niño")
    case 3:
        print("Usted es adolecente")
    case 4:
        print("Usted es adulto")
    case 5:
        print("Usted es mayor de edad")
