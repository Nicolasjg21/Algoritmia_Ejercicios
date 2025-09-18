# Nombre: Programa para retirar un monto de un saldo disponible.

# Entradas:
# saldo: Variable creara para indicar el saldo disponible en el banco.
# saldo_retiro: Variable hecha para indicar el monto del retiro.
# Salidas:
#   retiro exitoso o no: Mostrar si el retiro solicitado fue exitoso segun el saldo de el usuario.

# Proceso: Por medio del retiro que el usuario solicite, se le podra realizar el retiro o no dependiendo del saldo existente.


saldo = 2000000
print(f"Su saldo actual es de ${saldo}")
saldo_retiro = float(input("Ingrese el monto que desea retirar: "))
while saldo_retiro <= saldo:
    saldo -= saldo_retiro
    if saldo_retiro.is_integer():
        print(
            f"Usted retiro: ${int(saldo_retiro)} ,su saldo total actual es: ${int(saldo)}"
        )
        break
    else:
        print(f"Haz retirado: ${saldo_retiro} su saldo total actual es: ${int(saldo)}")
    if 0 == saldo:
        print(
            "Haz retirado todo el saldo disponible de tu cajero. Gracias por contactar con nostros"
        )
        break
    else:
        saldo_retiro = float(input("Ingrese el monto a retirar: "))
