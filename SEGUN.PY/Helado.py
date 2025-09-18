# Nombre: Programa para definir que precio de helado quiere y que puede pedir.

# Entradas:
# sabor = Definir cual el precio que va a escoger.


# Salidas:
#   El usuario obtendra sus posibilades segun el precio seleccionado en el menu.

# Proceso: Por medio del precio que escoja el usuario, se le brindan posibilidades de añadir
# de manera limitada segun su seleccion.

print(
    """
======== PRECIOS DE HELADOS ========
1. Helado Pequeño - 2.500.
2. Helado Pequeño Doble - 3.500.
3. Helado Mediano - 5.500.
4. Helado Grande - 7.000.
5. Copa Helado Grande 3 - 11.000.
======================
"""
)


sabor = int(input("¿De que precio quiere su helado?: "))
match sabor:
    case 1:
        print("Su helado puede ser de: Coco, Ron con pasas, fresas")
    case 2:
        print("Sus helados pueden ser de: Coco, Ron con pasas, fresas")
    case 3:
        print(
            "Su helado puede ser de: Coco, Ron con pasas, fresas, Maracuya, Limon Galleta, Tres leches + salsas"
        )
    case 4:
        print(
            """Su helado puede ser de: Coco, Ron con pasas, fresas, Maracuya, Limon Galleta,
              Tres leches, Brownie, Cokies and Cream + salsas + cualquier/1topping"""
        )
    case 5:
        print(
            """Su helado puede ser de: Coco, Ron con pasas, fresas, Maracuya, Limon Galleta,
              Tres leches, Brownie, Cokies and Cream + salsas y cualquier/5 toppings"""
        )
