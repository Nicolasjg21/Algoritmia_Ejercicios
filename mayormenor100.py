# Nombre: Programa para definir si un numero es mayor a 100  o menor de -100.

# Entradas:
#   Numero: Guardar el numero que digite el usuario.


# Salidas:
#   Confirmacion de rango: Verificar si el numero digitado se encuentra en el rango de 100 a -100.

# Proceso: Definir si el numero digitado se encuentra en el rango de 100 a -100, si no se encuentra en el rango el numero es mayor a 100  o menor de -100.

numero = int(input("Escriba un numero: "))
if numero > 100 or numero < -100:
    print("El numero esta fuera del rango de -100 a 100")
else:
    print("El numero esta en el rango de -100 a 100")
