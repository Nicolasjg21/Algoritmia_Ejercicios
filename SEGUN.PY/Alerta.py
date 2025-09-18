# Nombre: Programa para seleccionar un nivel de alerta segun su relevancia e importancia.

# Entradas:
# Alertas = variable para seleccionar la urgencia que necesita el usuario.


# Salidas:
#   El usuario sera atentido segun su proridad de emergencia.

# Proceso: Por medio del numero que digite el usuario, se tendra en cuenta para brindar su respecttiva alerta.

print(
    """
===================================== NIVELES DE EMERGENCIA =====================================
======== (Recuerde, sea conciente de su elecion, puede ser penitenciado en caso de no ser cierto) 

1.Ayuda nivel 1
2.Ayuda nivel 2
3.Ayuda Nivel 3
=================================================================================================
"""
)


Alertas = int(input("""Que tipo de ayuda necesita usted: """))
match Alertas:
    case 1:
        print(
            "lo pasaremos a la lista de espera, si no es mucha molestia, brindenos un momento."
        )
    case 2:
        print(
            "Ust esta en la fila prioritaria, porfavor sea paciente, seran unos minutos."
        )
    case 3:
        print(
            "Ust tiene gran importancia, brindenos unos segundos para estar en contacto con ust "
        )
