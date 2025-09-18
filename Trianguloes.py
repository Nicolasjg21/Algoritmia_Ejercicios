# Nombre: Programa para definir un tipo de triangulo.

# Entradas:
#   lado1: Guardar el primer lado del triangulo.
#   lado2: Guardar el segundo lado del triangulo.
#   lado3: Guardar el tercer lado del triangulo.


# Salidas:
#   Confirmacion: Comprobar que tipo de triangulo es segun sus lados.

# Proceso: El sistema concluira que tipo de triangulo es segun su == or != de el valor de sus lados.

lado1 = float(input("Ingrese el primer lado del triangulo: "))
lado2 = float(input("Ingrese el segundo lado del triangulo: "))
lado3 = float(input("Ingrese el tercer lado del triangulo: "))

if lado1 == lado2 and lado2 == lado3:
    print("Su triangulo es equilatero")
elif lado1 != lado2 and lado1 != lado3 and lado3 != lado2:
    print("Su triangulo es escaleno")
else:
    print("Su triangulo es isosceles")
