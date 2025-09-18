# Nombre: Programa para validarun tipo de triangulo.

#  Entradas
#     lado1, lado2, lado3: Variables asignadas para guardar el valor de cada dato.

#  Salidas:
#   tipo de triangulo: Por descarte el sistema hayara su triangulo

#  Proceso: El sistema mostrara un menu con los tipos de triangulos que puede analizar, el le pedira los lados de su triangulo
# y segun las opciones que usted escoja del menu, el hara el calculo y le dira si el triangulo es o no es lo que usted seleccione

print(
    """
================== TRIANGULOS ==================
1. Equilatero
2. Escaleno
3. Isoceles
      """
)

lado1 = float(input("Ingrese el primer lado del triangulo: "))
lado2 = float(input("Ingrese el segundo lado del triangulo: "))
lado3 = float(input("Ingrese el tercer lado del triangulo: "))

trianguloes = int(input("Mi triangulo es?: "))

match trianguloes:
    case 1:
        if lado1 == lado2 == lado3:
            print("Su triangulo es Equilatero")
        else:
            print("Su triangulo no es equilatero, pruebe otra opcion")
    case 2:
        if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            print("Su triangulo es escaleno")
        else:
            print("Su triangulo no es ecaleno, pruebe otra opcion")
    case 3:
        print("Su triangulo es isoceles")
