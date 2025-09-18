# Nombre: Programa para identificar que transporte uso segun la distancia recorrida.

# Entradas:
# tipotra: Variable que almacena la opcion seleccionada (los km reocrridos).

# Salidas:
#   Tipo de transporte: El programa definira cual pudo haber sido su medio
# de trasporte que uso para llegar segun su seleccion.

# Proceso: Por medio del numero que digite el usuario se deducira como se trasporto al estadio.
print(
    """
==== LISTA DE INVITADOS ====
1. 2 - 5 PERSONAS
2. 6 - 12 PERSONAS
3. 13 - 30 PEROSNAS
4. 30 - 50 PERSONAS
5. 60 o + PERSONAS
      """
)

tipotra = int(input("¿CUANTAS PERSONAS CONFROMAN SU LISTA DE INVITADOS?: "))
match tipotra:
    case 1:
        print(
            "Ust probablemente esta organizando una reunion bastante casual(Ejem: Un almuerzo.)"
        )
    case 2:
        print(
            "Ust probablemente esta organizando un junte casual(Ejem: Un Picnic, Una Reunion de Cumpleaños.)"
        )
    case 3:
        print(
            "Ust probablemente esta organizando algun tipo de fiesta o una reunion mediana(Ejem: Fiesta de Cumpleaños, Asado.)"
        )
    case 4:
        print(
            "Ust probablemente esta organizando un evento grande(Ejem: Un Baby Shower, Un cumpelaños especial.)"
        )
    case 5:
        print(
            """Ust probablemente esta orgamizando un evento de clase especial u formal
              (Ejem: Boda o Matrimonio, Cena de gala, Reunion familiar(todos o la mayoria de integrantes)) """
        )
