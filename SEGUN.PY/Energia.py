# Nombre: Programa para conocer el tipo de energia que usa el usuario segun su seleccion.

# Entradas:
# energia: Variable que conserva la seleccion del menu del usuario.

# Salidas:
#   confirmacion de energia: Segun la seleccion de la persona,
# se le compartira la energia que probablemente use.

# Proceso: El usuario seleccionara una de las opciones para
# confirmar el tipo de energia que probablemente usa.

print(
    """
======== ¿UST REALIZA O SE IDENTIFICA CON ALGUNA DE LAS OPCIONES? ========
1.Pago mi recibo de electricidad mensualemnte. 
2.Uso la energia del sol para obtener mi energia. 
3.Por medio de movimiento genero energia. 
4.No uso energia, solo soy productivo mientras halla luz.
==========================================================================
"""
)

energia = int(input("¿Cual escoge?: "))
match energia:
    case 1:
        print("Su tipo de energia es Electrica.")
    case 2:
        print("Su tipo de energia es Solar.")
    case 3:
        print("Su tipo de energia es Mecanica.")
    case 4:
        print("Su tipo de energia es Luminosa.")
