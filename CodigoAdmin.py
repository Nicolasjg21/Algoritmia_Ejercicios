# Nombre: Programa para darle acceso a los usuarios " Admin " por medio de un codigo.

# Entradas:
#   Administrador: Codigo respectivo para el administrador.


# Salidas:
#   Codigo correcto para el admin o no: El sistema reconoce si el codigo para los admins es el indicado o no.

# Proceso: El administrador ha de poner su codigo asignado, si el codigo es != no podra ingresar.

administrador = str(input("ingrese su codigo: "))
if administrador == "18273654":
    print("Bienvenido")
else:
    print("Denegado")
