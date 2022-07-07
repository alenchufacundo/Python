from verificarNumero import esDigito #se importo otra funcion de otro archivo

def mostrarMenu ():
    print("1-Agregar alumno")
    print("2-Eliminar alumno")
    print("3-Modificar alumno")
    print("4-Ver lista de alumnos")
    print("5-Salir")
    
    opcion = int(input("Seleccione una opcion: "))
    return opcion

def agregarAlumno():
    nombre = input("Ingrese nombre del alumno: ")
    nota = int(input("Ingrese la nota: "))
    alumnos[nombre] = nota
    
def eliminarAlumno():
    nombre = input("Ingrese el alumno a eliminar: ")
    alumnos.pop(nombre)

def modificarAlumno():
    nombre = input("Ingrese el nombre del alumno que desea modificar: ")
    nota = int(input("Ingrese la nota nueva que desea colocar: "))
    alumnos[nombre] = nota

#recorre el diccionario/array->si pongo print alumno->imprime los nombre. Y si pongo alumnos[alumno] imprime los valoers que tiene cada alumno.
def mostrarAlumnos():
    for alumno in alumnos:
        print(alumno,"->",alumnos[alumno])    

#verificarNumero.py #FUNCION en bucle para preguntar constantemente hasta que el usuario coloque la opcion valida.
def opcionValida():
    valida = False
    while valida == False:
        opcion = input("Seleccione una opcion del 1-5: ")
        longitudOpcion = len(opcion)##longitud del input de la opcion
        if (longitudOpcion == 1) and (esDigito(opcion)) and (opcion >='1') and (opcion <='5'):#todas las condiciones que debe cumplir
            return int(opcion)
        else:
            print("Error, ingrese un numero de 1 a 5 y de un solo digito")
        valida = esDigito(opcion)
        if(valida == False):
            print("Error, coloque un numero del 1 al 5")            
    return int(opcion)

alumnos = {}

op = 0
while(op !=5):
    opcionValida()
    op = mostrarMenu()
    if (op ==1):
        agregarAlumno()
    elif(op == 2):
        eliminarAlumno()
    elif(op == 3):
        modificarAlumno()
    elif(op == 4):
        mostrarAlumnos()
    elif(op == 5):
        print("Fin del programa")

