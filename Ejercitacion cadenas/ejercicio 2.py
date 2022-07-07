frase = input("ingrese una frase sin agregar espacios extras al final: ")
espaciosFrase = frase.count(" ")
caracteresFrase = len(frase)

#letras de frase exluyendo los espacios
print("la cantidad de letras que hay en la frase es: ", caracteresFrase - espaciosFrase)

#cantidad de palabras
contador = 0
cantidadPalabras = 1
while contador < espaciosFrase:
    contador += 1
    cantidadPalabras += 1
print(cantidadPalabras,"palabras")
# f = input("ingrese frase")
# ce = f cont(" ")
# cp = ce +1
# l = len(f) -ce
# print(f,"tiene",cp,"y",l,"letras")

