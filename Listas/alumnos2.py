nombre = "a"
alumnos = []

while (nombre != "0"):
    nombre = input("Ingrese nombre: ")  
    if (nombre != "0"):
        alumnos.append(nombre.title())
print(alumnos)

nombre2 = input("Ingrese nombre de alumno a buscar: ")
aparicion = alumnos.count(nombre2)
if (aparicion == 0):
    print("El alumno",nombre2.title(), "no se pudo encontrar")
else:
    print("El alumno",nombre2.title(), "se encuentra",aparicion,"de veces")
    pos = alumnos.index(nombre2)
    print("se encuentra en la posicion",pos+1)