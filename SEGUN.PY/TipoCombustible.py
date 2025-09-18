# Nombre: Programa para definir que tipo de combustible necesita su vehiculo.

# Entradas:
# combustible = Definir cual es tu tipo de vehiculo.


# Salidas:
#   El usuario obtendra su tipo de combustible segun su tipo de vehiculo.

# Proceso: Por medio del tipo de vehiculo que escoja el usuario, se le brinda el tipo de combustible que necesita.

print(
    """
================ VEHICULOS ====================
1. Buses de transporte público, Camiones de carga, Busetas y microbuses.
2. Carros familiares, Motos, Taxis.
3. Carros deportivos, Camionetas de alta gama, Vehículos de lujo o importados.
===============================================
"""
)


combustible = int(input("¿Que vehiculo usa usted?: "))
match combustible:
    case 1:
        print(" Su vehiculo necesita Diesel. ")
    case 2:
        print(" Su vehiculo necesita corriente. ")
    case 3:
        print(" Su vehiculo necesita Extra. ")
