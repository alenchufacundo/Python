class Vehiculo:
    def encender(self):
        print("Prendi el motor de combustible")

class VehiculoHibrido(Vehiculo):
    def encender(self):
        super().encender() #al agregarle super() al metodo encender() -> hace que hace referencia al metodo de la clase padre, la que hereda. Depende el lugar donde se encuentre
        print("Prendi el motor hibrido")

v = VehiculoHibrido()
v.encender() #entonces al llamar al metodo, ejecuta tanto el metodo padre como el propio. No se sobrescribe.