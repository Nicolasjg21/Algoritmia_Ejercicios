# Nombre: Programa para conocer el tipo de fiebre que el usuario tiene segun su seleccion.

# Entradas:
# energia: Variable que conserva la seleccion del menu del usuario.

# Salidas:
#   confirmacion de temperatura corporal: Segun la seleccion de la persona,
# se le compartira que tan preocupante es su temperatura corporal.

# Proceso: El usuario seleccionara una de las opciones para
# confirmar la relevancia de su temperatura corporal.

print(
    """
======== TEMPERATURAS CORPORALES ========
1.< A 37.5. 
2.De 37,5 - 38°c. 
3.De 38°c - 39°c
4.> 39°c
==============================
"""
)

TemperaturaC = int(input("QUE TEMPERATURA CORPORAL TIENE EN ESTE MOMENNTO: "))
match TemperaturaC:
    case 1:
        print("Usted tiene la temperatura corporal bien.")
    case 2:
        print("Usted tiene fiebre excesivamente leve.")
    case 3:
        print("Usted tiene fiebre modeada, es de cuidado.")
    case 4:
        print(
            "Usted tiene fiebre bastante alta, dirigase a un profesional urgentemente"
        )
