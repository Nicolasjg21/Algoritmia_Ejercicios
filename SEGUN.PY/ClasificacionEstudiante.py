# Nombre: Programa para seleccionar un valor a una
# cantidad de puntos correctos.

# Entradas:
# ValorNota: Variable hecha para escoger el rango donde se encuentra
# la cantidad de puntos correctos que obtuvo.


# Salidas:
#   Seleccion de un valor: Se le asignara un valor a los puntos correctos obtenidos
#   segun la opcion seleccionada.

# Proceso: Por medio del numero que digite el usuario acorde a la cantidad de puntos
# que obtuvo, se le brindara una nota congruente.


print(
    """
================== ¿Cuantos puntos tuvo bien? ==================
1. 1 punto de 5
2. 2 puntos de 5
3. 3 puntos de 5
4. 4 puntos de 5
5. 5 puntos de 5
      """
)


ValorNota = float(
    input(
        "Ingrese la opcion donde se encuentre la cantida de puntos correctos que obtuvo: "
    )
)
match ValorNota:
    case 1:
        print("Su nota es de 2.0")
    case 2:
        print("Su nota es de 4.0")
    case 3:
        print("Su nota es de 6.0")
    case 4:
        print("Su nota es de 8.0")
    case 5:
        print("Su nota es de 10.0")
