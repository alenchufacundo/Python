class Mascota: #clase padre
    def comer(self):
        print('La mascota come')
    
    def dormir(self):
        print('La mascota duerme')

class Felino:
    def cazar(self):
        print('El felino esta cazando')

class Gato(Mascota,Felino): #clase hija que hereda de padre.
    pass

kali = Gato()

kali.comer()
kali.dormir()
kali.cazar()