
nombreApellido = input("Ingrese su nombre y apellido: ")
vocales = ["a","e","i","o","u"]

cantidadVocales = 0
for c in nombreApellido:
    for i in range(0,len(vocales)):
        if c in vocales[i]:
            cantidadVocales += 1
print ("La cantidad de vocales es de: ",cantidadVocales)
print (nombreApellido.title())
