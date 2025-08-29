# Nombre: Programa para definir si un numero es negativo.

# Entradas:
#   Numero: Guardar el numero que digite el usuario.


# Salidas:
#   Confirmacion: Comprobar si el numero digitado es negativo o no.

# Proceso: El sistema concluira si el numero que el usuario digito es negativo o no.

numero = int(input("Escriba un numero: "))

if numero < 0:
    print("El numero es negativo.")
else:
    print("El numero es positivo.")
