socios = ["luisina","benjamin","lucia","isabella","nicolas","agustin"]
edad  = [13, 15, 10, 8, 16, 15]

contador = 0
while contador == 0:  
    nombre = input("Ingrese un nombre: ").lower()
    aparece = socios.count(nombre)
    if (aparece >= 1):
        posicionSocios = socios.index(nombre)
        print("La edad de",nombre.title(),"es de",edad[posicionSocios],"años")
        contador += 1
    else:
        print("El nombre",nombre.title(),"no se encuentra")

