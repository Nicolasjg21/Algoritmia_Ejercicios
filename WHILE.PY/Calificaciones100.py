# Nombre: Programa para ingresar notas de los estudiantes.

# Entradas:
# num: Variable hecha para depositar la nota del estudiante.

# Salidas:
#   Confirmacion nota ingresada: Mostrar que la nuta fue ingresada siempre y cuando sea minima o igual a 100.

# Proceso: Por el cual, el usuario podra anexar las notas que desea ingresar, siempre y cuando sea razonable. ( la nota no puede ser mas de 100.)

num = int(input("Ingrese las notas del estudiante: "))
if num <= 100:
    print("Su nota fue anexada")
while num <= 100 and num >= 1:
    num = int(input("Ingrese la nota del siguiente estudiante: "))
    print("Su nota fue anexada")
    if num > 100:
        print(
            " No es posible obtener una calificacion mayor a 100, vuelva a intentarlo "
        )
    if num <= 0:
        print("gracias por ingresar sus notas regrese pronto")
