# Nombre: Programa para definir si una temperatura congela.

# Entradas:
#   Temperatura: Guardar la temperatura que digite el usuario.


# Salidas:
#   Confirmacion: Comprobar si la temperatura del usuario congela o no.

# Proceso: El sistema concluira si la temperatura que el usuario digito congela o no.

temperatura = float(input("Ingrese la temperatura: "))
if temperatura <= 0:
    print("Si congela")
else:
    print("No congela")
