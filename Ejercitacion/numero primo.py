numero = int(input("ingrese numero hasta maximo 20: "))
if numero <= 20:
    for i in range(1,20):
        if (numero % i == 0):
            print (i)
            if (numero % numero  == 0) and (numero % i == 0):
                print("el numero",numero," es primo")
else:
    print("Error al ingresar el numero")
