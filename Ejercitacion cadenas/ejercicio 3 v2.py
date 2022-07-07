nombreApellido = input("ingrese un nuevo y apellido: ")
vocales = ["a","e","i","o","u","A","E","I","O","U"]

cantidadVocales = 0
for letra in nombreApellido:
    if letra in vocales:
        cantidadVocales += 1
print("cantidad de vocales:",cantidadVocales)


#nombre = input("ingrese")
#apellido = input("ingrese")
#contador = 0
#for letra in nom:
#   if letra in "aeiouAEIOU"
#       contador +=1
#for letra in apel:
#   if letra in "aeiouAEIOU"
#   contador +=1
#print(nombre.capitalize(),apellido.capitalize(),contador)
#
