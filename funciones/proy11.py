def esdigito(caracter):
    if (caracter>='0' and caracter<='9'):
        return True
    else:
        return False

def opcionvalida():
    valida=False
    while valida==False:
        op=input("Seleccione opción: ")
        valida=esdigito(op)
        c=len(op)
        if c==1 and esdigito(op) and (op>='1') and (op<='5'):
            return int(op)
        else:
            print("Valor erróneo")
    

def mostrarmenu():
    print("1.Agregar alumno")
    print("2.Eliminar alumno")
    print("3.Modificar alumno")
    print("4.Ver lista alumnos")
    print("5.Salir")
    op=opcionvalida()
    return op

def agregaralumno():
    nom=input("Ingrese nombre de alumno: ")
    nota=int(input("Ingrese su nota: "))
    alumnos[nom]=nota

def eliminaralumno():
    nom=input("Ingrese el nombre del alumno que desea eliminar")
    alumnos.pop(nom)

def modificaralumno():
    nom=input("Ingrese nombre de alumno: ")
    nota=int(input("Ingrese nueva nota: "))
    alumnos[nom]=nota

def mostrarlista():
    for a in alumnos:
        print(a,"-",alumnos[a])


print(esdigito('A'))
alumnos={}
o=0
while o!=5:
    o=mostrarmenu()
    if o==1:
        agregaralumno()
    if o==2:
        eliminaralumno()
    if o==3:
        modificaralumno()
    if o==4:
        mostrarlista()