class Cuadrado:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def obtenerArea(self):
        self.area = self.base * self.altura

class Figura(Cuadrado):
    def obtenerArea(self):
        pass
