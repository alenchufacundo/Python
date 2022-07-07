class Usuario:
    def __init__(self):
        self.nombre = "Facundo"
    
    def presentarse(self):
        print(self.nombre)
    
    def asignarApodo(self, nombreNuevo):
        self.nombre = nombreNuevo

class Tutor (Usuario): #crea una nueva clase y hereda la clase Usuario
    def asignarClase(self, nombreClase):
        self.clase = nombreClase

    def iniciarClase(self):
        print("hoy empieza la clase",self.clase)


#-----------------------
facundo = Tutor()
facundo.asignarClase("POO")
facundo.iniciarClase()



#instancio objeto
#usuarioNuevo = Usuario()
#usuarioNuevo.asignarApodo("gordo")
#usuarioNuevo.presentarse()
