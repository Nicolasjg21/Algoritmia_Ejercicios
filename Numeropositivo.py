# Nombre: Programa para definir si un numero es positivo.

# Entradas:
#   Numero: Guardar el numero que digite el usuario.


# Salidas:
#   Confirmacion: Comprobar si el numero digitado es positivo o no.

# Proceso: El sistema concluira si el numero que el usuario digito es positivo o no.

numero = int(input("Escriba un numero: "))
print(numero)
if numero > 0:
    print("El numero es positivo.")
else:
    print("El numero es negativo.")
