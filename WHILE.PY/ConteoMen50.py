# Nombre: Programa para realizar un conteo de numeros menores al numero 50.

# Entradas:
# num: Variable hecha para almacenar el numero escrito por el usuario.
# contador: Variable que se encarga de almacenar el numero de veces que se escribio un numero menor a 50.
# resultado: ayudante, funciona para realizar el calculo exacto del contador.
# Salidas:
#   Confirmacion de vehiculo: Cuando el usuario decida cerrar el programa ( digitando un numero mayor o igual a 50),
# se le mostrara el numero de veces que digito un numero menora 50.

# Proceso: Por medio del numero que digite el usuario se realizara el conteo hasta que el usuario lo desee y
# se le compartira la canitidad de veces que digito un numero menor a 50.


contador = 0
num = 0
while num <= 50:
    contador = contador + 1
    resultado = contador
    resultado = resultado - 1
    num = int(input("Ingrese un numero (Ingrese un numero mayor a 50 para salir): "))
print("La cantidad de numeros ingresados menores a 50 fueron: ", resultado)
