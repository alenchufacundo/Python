#creacion de la clase con sus metodos(funciones) y propiedaes (variables)
class Alarma:
    #define el metodo constructor
    def __init__(self,fecha_alarma): #aca en el constructor se le pone un parametro
        #define un atributo/propiedad  de la clase
        self.fecha_programar = fecha_alarma #a esta atribute se le define ese parametro
    #define un metodo/funcion
    def programar(self):
        print("hola")

#----------------------------------------------------------------

#instancia un objeto de la clase Alarma ->crea un objeto
alarma = Alarma("03/10/1996") # se llama a la clase y se le pasa un parametro
#objeto.propiedad
print(alarma.fecha_programar)