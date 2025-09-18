# Nombre: Programa para realizar la secuencia de Fabonacci.

# Entradas:
# num1: }
# num2: } Variables asignadas para realizar las secuencias atomaticas, apartir de de num1 y num 2.
# num3: }
# Limite: Variable que guarda el limite depositado por el usuario para la seccuencia.

# Salidas:
#   Secuencia Creada: Segun el numero limite digitado, se realizara la secuencia.

# Proceso: Segun el numero limite digitado por el usuario, se realizara el calculo y la secuencia.


limite = int(input("Ingrese el valor limite: "))
num1 = 0
num2 = 1
while num1 <= limite:
    print(num1)
    num3 = num1 + num2
    num1 = num2
    num2 = num3
print("Su secuencia fue creada")
