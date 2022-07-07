cantidadNombres = int(input("¿Cuantos alumnos desea ingresar?: "))
alumnos = [] #creo un arreglo vacío.

for i in range (0, cantidadNombres, 1):
    #0= donde inicia, cantidadNombres = donde termina, y 1 = el incremento)
    #no se le pone el cantidadNombres + 1 porque quiero que vaya del 0,1,2,3,4(ahi tengo los 5)
    #la i en la primer vuelta vale 0,despues 1, 2 ,3.
    nombre = input("Ingrese un nombre: ")
    # alumnos.insert(i,nombre) ->la i es la posicion que explique arriba, y luego el 2nd parametro lo q quiero agregar.
    alumnos.append(nombre)
alumnos.append("Christian")
alumnos.sort()
print(alumnos)
cantidadAlumnos = len(alumnos)
print("usted tiene",cantidadAlumnos,"alumnos cargados")
