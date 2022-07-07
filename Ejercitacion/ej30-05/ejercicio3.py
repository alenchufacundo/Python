nombre = input("Ingrese su nombre: ")
fechaNac = input("Ingrese su fecha de nacimiento en este formato dia/mes/año: ")
anioNac = int (fechaNac[-4:])

if (anioNac >= 1920 and anioNac <= 1945):
    print(nombre,"nacio en el",fechaNac[-2:],"y pertenece a la Generacion Silenciosa")
elif(anioNac > 1946 and anioNac < 1964):
    print(nombre,"nacio en el",fechaNac[-2:],"y pertenece a la Generacion BabyBoomers")
elif(anioNac > 1965 and anioNac < 1979):
    print(nombre,"nacio en el",fechaNac[-2:],"y pertenece a la Generacion X")
elif(anioNac > 1980 and anioNac < 1999):
    print(nombre,"nacio en el",fechaNac[-2:],"y pertenece a la Generacion Y o Milenials")
elif(anioNac > 2000 and anioNac < 2010):
    print(nombre,"nacio en el",fechaNac[-2:],"y pertenece a la Generacion Z o Centenials")
elif(anioNac > 2000):
    print(nombre,"nacio en el",fechaNac[-2:],"y pertenece a la Generacion Alfa")