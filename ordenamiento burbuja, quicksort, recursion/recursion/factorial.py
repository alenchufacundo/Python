#funcion para calcular el factorial de un numero con recursion, que es lo mas ideal.
#el factorial de un numero es un entero positivo que es el producto de todos los numeros anteriores o igaules a él.
#ejemplo -> 5 = 5 * 4 * 3 * 2 * 1 -> esto da como resultado 120 si se multiplican uno por uno.
#se escribe n! y el factorial de 0 es 1.




#modo facil sin recursion
def factorial(numero):
    producto = 1
    for i in range(1,numero + 1): #aca es el n + 1 porque toma el numero anterior a numero. ejemplo: si es 5, toma el 4. #va de 1 porque el 0 no es multiplicable.
        producto = producto * i
    return producto


# print(factorial(5))

#como hacerlo recursivo?
def factorialRecursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorialRecursivo(numero - 1)

print(factorialRecursivo(5))