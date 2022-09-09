

class Animal: #clase padre
    def comer(self):
        print('El animal come')
    
    def dormir(self):
        print('EL animal duerme')


class Mascota(Animal): #clase padre hereda de animal
    def comer(self): #sobrescribrio el metodo comer de la clase animal.
        print('la mascota come') 

class Felino:
    def cazar(self):
        print('El felino esta cazando')

class Gato(Mascota,Felino): #clase hija que hereda de padre.
    def __init__(self,nombre):
        self.nombre = nombre

    def comer(self):
        super().comer() #el super aca sirve para que se pueda usar el metodo padre sin que se sobrescriba.
        print(f'{self.nombre} come')


kali = Gato('kali')
kali.comer()
kali.dormir()

