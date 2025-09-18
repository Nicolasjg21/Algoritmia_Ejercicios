# Nombre: Programa para seleccionar una seccion de dispositivos usados en un sitio .

# Entradas:
# dispositivos: Variable hecha para almacenar el numero de seccion el usuario.

# Salidas:
#   Seleccion de algun dispositivo.

# Proceso: Por medio del numero que digite (1-4), a el usuario se le presentara la seccion de dispositivos seleccionada .

dispositivos = int(
    input("Digite un numero del 1 al 4 para conocer los dispositivos que manejamos")
)
match dispositivos:
    case 1:
        print("Celulares")
    case 2:
        print("Tablets")
    case 3:
        print("Computadores")
    case 4:
        print("Consolas")
    case _:
        print("Su numero digitado no se encuentra en las secciones.")
