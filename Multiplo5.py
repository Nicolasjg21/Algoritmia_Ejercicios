# Nombre: Programa para definir si un numero es multiplo de 5 o no.

# Entradas:
#   Numero: Guardar el numero que digite el usuario.


# Salidas:
#   Confirmacion: Comprobar si el numero es multiplo o no.

# Proceso: Definir si el numero digitado es multiplo del numero 5.

numero = int(input("Ingrese numero: "))
if numero % 5 == 0:
    print("El numero es multiplo de 5")
else:
    print("El numero no es multiplo de 5")
