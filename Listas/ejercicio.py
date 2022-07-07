numeroTelefono = (input("Ingrese su numero de telefono con sus caracteristicas entre parentesis (XXX)XXXXXXX: "))
cantidadNumeroTelefono = len(numeroTelefono)
if (cantidadNumeroTelefono == 12):
    print("15" + numeroTelefono[5:12])
else:
    print("Error, ingreso un numero inexistente")