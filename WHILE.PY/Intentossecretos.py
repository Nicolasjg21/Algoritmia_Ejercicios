# Nombre: Programa para realizar el conteo de intentos gastados por un usuario.

# Entradas:
# contraseña: Variable hecha para almacenar las combinaciones digitadas por el usuario.
# contador: Variable creada para almacenar # de intentos del usuario
# Salidas:
#   Confirmacion de vehiculo: Una vez el usuario acerte la combinacion se le compartira cuantos intentos obtuvo.

# Proceso: Por medio de la combinacion que digite el usuario obtendra el conteo de intentos hasta que acerte.


contador = 0
contraseña = "4567"
num = int(input("""Digite una combianacion de 4 numeros para acceder (Del 1 al 9): """))
while num != contraseña:
    contador = contador + 1
    num = input("Incorrecto, ingrese otra combinacion: ")
print(
    "Felicidades usted ha hallado la combinacion en:", contador, "intentos, Bienvenido"
)
