# Nombre: Programa para seleccionar una seccion de productos.

# Entradas:
# productos: Variable hecha pa almacenar numeros seleccionados por el user respectivos al dispsitivo que escoja el usuario.

# Salidas:
#   Confirmacion de producto: Al momento de escoger un numero, el numero estara de la mano con el producto al cual fue asignado.

# Proceso: Por medio del numero que digite la persona se asignara una seccion de dispositivos.

productos = int(
    input(" Digite un numero del 1 al 5 para conocer las categorias de los productos: ")
)
match productos:
    case 1:
        print("Electronicos")
    case 2:
        print("Ropa")
    case 3:
        print("Alimentos")
    case 4:
        print("Hogar")
    case 5:
        print("ElectronJuguetesicos")
    case _:
        print("Su numero digitado no se encuentra en las categorias de los prductos.")
