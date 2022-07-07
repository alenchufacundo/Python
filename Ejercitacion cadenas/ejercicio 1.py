palabra = input("Ingrese una palabra: ")
caracteresPalabra = len(palabra)
contador = 0
while contador < caracteresPalabra:
    if contador % 2 == 0:
        print(palabra.upper())
    else:
        print(palabra.lower())
    contador += 1

#for i in range(1,caracteresPalabra+1,1)(inicio indice, fin indice, es mas 1 porque si se pone el fin, no incluye el ultimo, incremento)
#    if i % 2 == 0:
#       print(palabra.upper())
#    else:
#       print(palabra.lower())


