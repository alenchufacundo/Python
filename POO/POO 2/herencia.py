class Mascota: #clase padre
    def comer(self):
        print('La mascota come')
    
    def dormir(self):
        print('La mascota duerme')

class Perro(Mascota): #clase hija que hereda de padre.
    def ladrar(self): # aca aclarar cosas especificas de la clase perro
        print('El perro ladra')


venus = Perro()

venus.comer()
venus.dormir()
venus.ladrar()
