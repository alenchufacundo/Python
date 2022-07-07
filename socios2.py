socios2 = {
    "luisina" : 1,
    "benjamin" : 3,
    "lucia" : 1,
    "isabella" : 1,
    "nicolas" : 2,
    "agustin" : 4
}

deporte = {
    1: "futbol",
    2: "basquet",
    3: "tenis",
    4: "voley"
}

contador = 0
while contador == 0:
    nombre = input("Ingrese el nombre de la persona que quiera saber que deporte practica: ")
    if nombre in socios2:
        value = socios2.get(nombre,"no se encuentra ese nombre")
        print(nombre,"practica",deporte[value])
        contador += 1
    else:
        print("el nombre",nombre,"no se encuentra")
        