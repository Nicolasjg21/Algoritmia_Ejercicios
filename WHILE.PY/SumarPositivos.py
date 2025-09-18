# Nombre: Programa para realizar la suma de numeros positivos digitados.

# Entradas:
# num: Variable hecha para almacenar los numero sque digite el usuario.
# suma: Variable encargada de sumar, solo si el numero es positivo.

# Salidas:
#   Sujma de numeros: Mostrar la suma de los numeros poritivos.

# Proceso: Por medio de los numeros que digite el usuario, obtendra una suma de solo los numeros positivos digitados.


suma = 0
num = int(input("Ingrese un numero(Ingrese uno negativo para salir): "))
while num >= 0:
    suma = suma + num
    num = int(input("Ingresar otro numero (Negativo para salir)"))
print("La suma de los numeros positivos es: ", suma)
