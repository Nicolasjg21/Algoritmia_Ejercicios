# Nombre: Programa para definir si un individuo tiene acceso al voto.

# Entradas:
#   Edad: Guardar ela edad del individuo.
#   Nacionalidad: guardar la nacionalidad del individuo.


# Salidas:
#   Confirmacion: Comprobar si el individuo puede votar segun los parametros.

# Proceso: El sistema concluira si el individuo a registrarse puede votar segun los parametros (18 años, nacionalidad Colombiana)
# de lo comntrario el usuario no tendra permitido el acceso al voto.

edad = int(input("Digite su edad: "))
nacionalidad = input("Digite su nacionalidad: ").capitalize()
if edad >= 18 and nacionalidad == "Colombiano":
    print("Ust puede votar")
else:
    print("Ust no puede votar")
