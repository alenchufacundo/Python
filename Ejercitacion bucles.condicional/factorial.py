numero = int(input("ingrese un numero entero: "))
numeroFactorial = 1

if numero > 0 and numero <= 10: 
    while numero != 0:
        numeroFactorial = numeroFactorial * numero
        numero = numero - 1
    print("el factorial es",numeroFactorial)
else:
    print ("incorrecto, el numero es negativo")

