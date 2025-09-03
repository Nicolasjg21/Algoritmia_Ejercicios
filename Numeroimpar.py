# Nombre: Programa para definir si un numero es par o impar.

# Entradas:
#   Numero: Guardar el numero que digite el usuario.


# Salidas:
#   Confirmacion: Comprobar si el numero digitado es par o impar.

# Proceso: El sistema concluira si el numero que el usuario digito es par o impar.

numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
