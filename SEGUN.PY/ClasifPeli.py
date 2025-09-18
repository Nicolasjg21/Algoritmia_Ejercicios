# Nombre: Programa para conocer las peliculas en cartelera segun su clasificacion.

# Entradas:
#   mensaje = Variable diseñada para crear el listado de clasificaciones para mostrar el usuario.
# calsificaciones: Variable hecha pa almacenar el numero de clasificacion que escoja el usuario.

# Salidas:
#   Confirmacion de peliculas: Mostrar las peliculas de la clasificaccion seleccionada.

# Proceso: Por medio del numero que digite el usuario segun la clasificaccion seleccionada, congruente a la eleccion se mostraran las peliculas para la edad.

mensaje = """
******CLASIFICACIONES: 1.Menores(7-14 años), 2.Adolecentes(14-17 años), 3.Mayores de edad(18-... años)******
"""
print(mensaje)

clasificaciones = int(
    input(
        "Digite un numero del 1 al 3 para conococer las peliculas segun la clasificacion por edades : "
    )
)
match clasificaciones:
    case 1:
        print("PELICULAS PARA NIÑOS: 1.My Little Ponny, 2. Cars , 3. Lilo y Stich")
    case 2:
        print(
            "PELICULAS PARA ADOLECENTES: 1.Advengers End Game, 2. Spiderman Far For Home , 3. It"
        )
    case 3:
        print(
            "PELICULAS PARA MAYORES DE EDAD: 1. terrifier, 2. 50 sombras de grey , 3. Destino final"
        )
    case _:
        print("Su numero digitado no se encuentra en las categorias de los prductos.")
