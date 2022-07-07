#creacion de la clase con sus metodos(funciones) y propiedaes (variables)
class Alarma:
    #define el metodo constructor
    def __init__(self): #este es el metodo constructor que se ejecuta automaticamente cuando se instancia un objeto
        #define un atributo/propiedad  de la clase
        self.fecha_de_alarma = "31-03-2022"
        self.color = "rojo"
        self.modelo = "casio"
        self.volumen = 0
        self.cantidadDeRuidos = 3
        self.apagado = False

    #define un metodo/funcion
    def programar(self):
        print("hola")

    def subir_volumen (self):
        self.volumen = self.volumen + 1 #self.volumen accede al atributo de self.volumen que es 0
    def bajar_volumen(self):
        self.volumen = self.volumen - 1
        
    #def hola (self):
        #pass #pass siginifca que la funcion esta vacia.

#----------------------------------------------------------------

#instancia un objeto de la clase Alarma ->crea un objeto
alarma = Alarma()
#objeto.propiedad
alarma.bajar_volumen() #invoca al metodo/funcion y hace que esto 0 = 0 + 1
print(alarma.volumen) #esto imprime lo de arriba.

#objeto.funcion/metodo
#alarma.programar()

#segundo objeto creado
#alarma_dos = Alarma()

