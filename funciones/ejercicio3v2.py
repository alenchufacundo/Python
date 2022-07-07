def esvocal(c):
    if len(c) == 1:
        vocales = "aeiou"
        c = c.lower()
        return c in vocales
    else:
        return False

hola = esvocal("o")
print(hola)