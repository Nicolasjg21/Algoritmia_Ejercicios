# Nombre: Programa para seleccionar una seccion de comida especifica y vizualizar su menu.

# Entradas:
#   mensaje = Variable diseñada para crear el listado de clasificaciones para mostrar el usuario.
#   type = variable dependiente de mostrar los diferentes platos a escoger segun su categoria seleccionada.

# Salidas:
#   Brindar informacion de el menu segun el numero seleccionado

# Proceso: Por medio del numero que digite  el usuario (1-4), se presentaran los platos de la seccion a desarrollar.

mensaje = """
======== MENU ========
1.Postres.
2.Cultura Colombiana.
3.Comida Vegetariana.
4.Comida animal de mar.
"""
print(mensaje)
Type = int(input("Digite del 1 al 4 el tipo de comida que desea: "))
match Type:
    case 1:
        print("Chese Cake, Red Velvet, Pie de Limon")
    case 2:
        print("Ajiaco, Bandeja Paisa, Sancocho Tri-Fasico, Arroz Atollado")
    case 3:
        print(
            "Curry de garbanzos, Hamburguesa vegetariana, Arepa llena de Champiñoes y Queso"
        )
    case 4:
        print("Casuela de Mariscos, Mojarra Frita, Bagre en Salsa")
    case _:
        print("Su numero no se encuentra en el menu")
