def esVocal (caracter):
    vocales = ["a","e","i","o","u"]
    if (caracter in vocales):
        return True
    else:
        return False

respuesta = esVocal("p")
print(respuesta)