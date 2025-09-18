# Nombre: Programa para seleccionar una seccion de vehiculos segun el # de llantas.

# Entradas:
# vehiculos: Variable hecha pa almacenar el numero de neumaticos que digite el usuario.

# Salidas:
#   Confirmacion de vehiculo: Mostrar la seccion segun el # de llantas.

# Proceso: Por medio del numero que digite (2-4), el usuario obtendra una seccion de vehiculos.


suma = 0
contador = 0
num = int(input("Ingrese un numero (Para salir ingrese un numero negativo): "))
while num > 0:
    suma = suma + num
    contador = contador + 1
    num = int(input("Ingrese un numero (Para salir ingrese un numero negativo): "))
    if contador > 0:
        promedio = suma / contador
        print("El promedio es: ", promedio)
    else:
        print("No se ingresaron numeros")
