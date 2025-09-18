# Nombre: Programa para realizar una suma de numeros hasta que el usuario desee.

# Entradas:
# num: Variable hecha para almacenar los numeros digitados por el usuario.
# suma: Variable encargada de operar.

# Salidas:
#   Suma: Mostrar la suama total de los numeros digitados.

# Proceso: Por medio del numero que digite el usuario obtendra una suma hasta el momento que el desee.


suma = 0
num = int(input("Ingrese un numero(Ingrese 0 para salir): "))
while num != 0:
    suma = suma + num
    if suma >= 100:
        print("Su suma ya es de 100 o mas: ", suma)
        break
    num = int(input("Ingrese un numero(Ingrese 0 para salir): "))
print("Programa finalizado, suma total = ", suma)
