# Nombre: Programa para realizar el conteo de numeros positivos digitados.

# Entradas:
# num: Variable hecha para almacenar el numero ingresado por el usuario.
# contador: Variable creada para realizar el conteo de los numeros positivos ingresados.

# Salidas:
#   Confirmacion de numeros: una vez el usuario decida cerrar el sistema se le mostrara la cantidad de veces que digito un numero positivo.

# Proceso: Por medio del numero que digite el usuario obtendra una cantidad de veces que digito un numero positivo hasta que el usuario decida finalizar el programa.


contador = 0
num = int(input("Ingrese un numero positivo ( Ingrese uno negativo para salir.): "))
while num >= 0:
    if num > 0:
        contador = contador + 1
    num = int(input("Ingrese un numero positivo ( Ingrese uno negativo para salir.): "))
print("La cantidad de numeros positivos ingresados fue: ", contador)
