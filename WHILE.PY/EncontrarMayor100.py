# Nombre: Programa para seleccionar un numero mayor a 100.

# Entradas:
# num: Variable hecha para que el usuario deposite el numero de su preferencia y ver si es util.

# Salidas:
#   Confirmacion de numero: Si el numero es mayor a 100 mostrara una respuesta, de lo contrario pedira un nuevo ingreso de otro numero.

# Proceso: Por medio del numero que digite el usuario obtendra una respuesta ( si su numero es mayora  100).


num = int(input("ingrese un numero: "))
while num < 100:
    print("El numero es muy pequeño")
    num = int(input("ingrese un nuevo numero: "))
print("El numero ingresado, mayor a 100 fue:", num)
