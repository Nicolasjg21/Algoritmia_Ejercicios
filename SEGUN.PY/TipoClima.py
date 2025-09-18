# Nombre: Programa para brindar informacion de su clima a partir de su temperatura.

# Entradas:
#   mensaje = Variable diseñada para crear el listado de preguntas para poder reconocerel clima.
#   tipoClima = variable dependiente de mostrar los diferentes tipos de clima
# segun la temperatura identificada por el usuario en las preguntas.

# Salidas:
#   Brindarle al usuario su clima actual.

# Proceso: Segun la temperatura identificada por el usuario, el usuario ha de seleccionar una opcion y sera revelado el clima actual

mensaje = """
======== MENU ========
1.¿Su temperatura es mayor a 24°c?.
2.¿Su temperatura esta entre 18°c y 24°c?.
3.¿Su temperatura es menor a 18°c?.
======================
"""
print(mensaje)

TipoClima = int(input("¿Como esta su clima?: "))
match TipoClima:
    case 1:
        print("Su clima es Calido")
    case 2:
        print("Su clima es Templado")
    case 3:
        print("Su clima es Frio")
