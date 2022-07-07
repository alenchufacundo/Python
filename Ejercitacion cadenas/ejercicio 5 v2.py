cadena = input("Ingrese una palabra: ")
sentidoIzq = 0
sentidoDer = len(cadena) - 1

if cadena[sentidoIzq] != cadena[sentidoDer]:
    print("no es palindromo")
else:
    while sentidoDer >= sentidoIzq:
        if cadena[sentidoIzq] == cadena[sentidoDer]:
            sentidoIzq += 1
            sentidoDer -= 1
    print("es palindromo")

