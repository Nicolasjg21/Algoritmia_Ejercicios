# Nombre: Programa para seleccionar un dia de la semana y saber cual es su frase diaria.

# Entradas:
# NumeroD = Variable para seleccionar el dia de la semana.
# mensaje = Menu que contiene los dias de la semana.

# Salidas:
#   El usuario obtendra su frase motivacinal segun su dia.

# Proceso: Por medio del numero que digite el usuario, conocera su frase motivacional del dia.

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

NumeroD = int(input("""Seleccione el dia de hoy para ver su frase diaria: """))
match NumeroD:
    case 1:
        print(
            """ "El único modo de hacer un gran trabajo es amar lo que haces." - Steve Jobs """
        )
    case 2:
        print(""" "Si puedes soñarlo, puedes lograrlo." - Walt Disney """)
    case 3:
        print(
            """ "El éxito es la suma de pequeños esfuerzos repetidos día tras día." - Robert Collier """
        )
    case 4:
        print(""" "Cree que puedes y ya estás a medio camino." - Theodore Roosevelt """)
    case 5:
        print(
            """ "No dejes que el miedo a perder sea mayor que la emoción de ganar." - Robert Kiyosaki """
        )
    case 6:
        print(
            """ "La vida es 10% lo que te sucede y 90% cómo reaccionas a ello." - Charles R. Swindoll """
        )
    case 7:
        print(
            """ "El futuro pertenece a quienes creen en la belleza de sus sueños." - Eleanor Roosevelt """
        )
