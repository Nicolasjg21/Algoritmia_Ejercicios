# Nombre: Programa para realizar una suma de numeros impares hasta el #50.

# Entradas:
# num: Variable hecha para almacenar los numeros de la suma.
# suma: Variable encargada de operar.

# Salidas:
#   Suma: Mostrar la suama total de los numeros impares.

# Proceso: Por medio del uan secuencia automatica el usuario obtendra una suma de numeros impares hasta el #50.


num = 1
suma = 0
while num <= 50:
    num = num + 2
    print(num)
    if num % 2 != 0:
        suma = suma + num
print("La suma de los numeros impares es: ", suma)
