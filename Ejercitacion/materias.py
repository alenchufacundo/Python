from dataclasses import asdict

asignaturas = ["matematicas","fisica","quimica","historia","lengua"]
notas = []
longitudAsignaturas = len(asignaturas)

for i in range(0,longitudAsignaturas):
    nota = input("Ingrese nota de la asignatura "+ asignaturas[i].title()+": ")
    notas.append(nota)

print("")

for i in range(0,len(notas)):
    print("Usted tiene en la asignatura:",asignaturas[i].title(),"un",notas[i])
