# Nombre: Programa para definir si un individuo aprobo o reprobo una nota.

# Entradas:
#   Numero: Guardar la nota que digite el usuario.


# Salidas:
#   Confirmacion: Comprobar si la nota es suficiente para aprobar, de lo contrario se reprobara.

# Proceso: El sistema concluira si la nota es suficiente para aprobar, de lo contrario se reprobara.

nota = float(input("Escriba su nota: "))
if nota >= 6:
    print("El estudiante aprobo")
else:
    print("El estudiante reprobo")
