# Nombre: Programa para seleccionar un tipo de documento y digitarlo para anexarlo en la base.

# Entradas:
# documento: Variable hecha para almacenar su tipo de documento y su numero de documento.

# Salidas:
#   Anexo de documento: Segun el documento que ust escoja, se le pedira su numero
# de documento y se anexara en la plataforma

# Proceso: El usuario seleccionara su tipo de documento y lo digitara para que el sistema lo anexe en la base de datos

print(
    """
======== TIPOS DE DOCUMENTO ========
1.Cedula de Ciudadania(C.C).
2.Tarjeta de Identidad(T.I).
3.Permiso de Proteccion Temporal(PPT)
4.Cédula de Extranjería(C.E)

======================
"""
)

documento = int(input("Cual es su tipo de documento: "))
match documento:
    case 1:
        cc = int(input("Digite su Cedula de Ciudadania: "))
        print("Su documento fue anexado")
    case 2:
        ti = int(input("Digite su Tarjeta de Identidad: "))
        print("Su documento fue anexado")
    case 3:
        ppt = int(input("Digite su Permiso de Proteccion Temporal: "))
        print("Su documento fue anexado")
    case 4:
        ce = int(input("Digite su Cedula Extranjera: "))
        print("Su documento fue anexado")
