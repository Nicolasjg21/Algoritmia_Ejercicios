# Nombre: Programa para identificar que transporte uso segun la distancia recorrida.

# Entradas:
# tipotra: Variable que almacena la opcion seleccionada (los km reocrridos).

# Salidas:
#   Tipo de transporte: El programa definira cual pudo haber sido su medio
# de trasporte que uso para llegar segun su seleccion.

# Proceso: Por medio del numero que digite el usuario se deducira como se trasporto al estadio.
print(
    """
================== DISTANCIA RECORRIDA ==================
1. 0 - 2 km.
2. 2 - 10 km.
3. 10 - 50 km.
4. 50 - 300 km.
5. 300+ km.
      """
)

tipotra = int(input("Que distancia recorrio para llegar al estadio?: "))
match tipotra:
    case 1:
        print("Ust probablemente llego al estadio a Pie o utilizo Bicicleta")
    case 2:
        print("Ust probablemente llego al estadio usando Bicileta o Moto")
    case 3:
        print("Ust probablemente llego al estadio usando Auto o Transporte Publico")
    case 4:
        print("Ust probablemente llego al estadio usando Autobus o Coche")
    case 5:
        print("Ust probablemente llego al estadio usando Avion o Tren")
