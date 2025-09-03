# Nombre: Programa para darle acceso a los usuarios " Admin ".

# Entradas:
#   rol: Variable asignada para definir el "Admin".


# Salidas:
#   Acceso solo para administradores: Si el usuario tiene un rol != a admin.

# Proceso: El sistema reconoce y permite el intgreso solo de "Administradores".


rol = str(input("Ingrese su rol (admin/usuario): "))
if rol == "admin":
    print("Bienvenido")
else:
    print("Denegado")
