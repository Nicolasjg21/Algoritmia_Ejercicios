# Nombre: Programa para conocer las sucursales de una tienda.

# Entradas:
# tienda: Variable que conserva la seleccion del menu del usuario
# (la sucurursal en la que esta interesado).

# Salidas:
#   Informacion de la sucursal: Segun la seleccion de la persona,
# se le compartira la informacion de la sucursal seleccionada.

# Proceso: El usuario seleccionara una de las opciones para
# obtener la informacion de la sucursal.

print(
    """
======== VNG-FILES.RYA - SEDES ========
1.Local Principal. 
2.Outlet. 
3.Centro Comerial Andino. 
4.Centro de Bogota D.C.
=======================================
"""
)

tienda = int(input("La sede que usted desea consultar es: "))
match tienda:
    case 1:
        print(
            "Zona T - Bogota(Kr 13 #87-56), Distribuidor principal del brend, horario(8Am-6:30Pm)."
        )
    case 2:
        print(
            "Plaza de Las Americas - Bogota(Cra 76d#8-96 sur), Tercera Sucursal Del Brend, horario(8Am-6:30Pm)."
        )
    case 3:
        print("Cra. 11 #82-71, Chapinero, Exclusive del brend, horario(10Am-7:30Pm).")
    case 4:
        print("Bogota(Cl 40a #67.), personalizaciones del brend, horario(8Am-6:30Pm).")
