class Ciudadano:
    def asignarNombre(self, nombres, apellidoPaterno, apellidoMaterno):
        self.nombreCompleto  = nombres + apellidoPaterno + apellidoMaterno 

class CiudadanoNorteamericano(Ciudadano):
    def asignarNombre(self,primernombre, primerApellido):
        self.nombreCompleto = primernombre + primerApellido #sobrescritura de metodo del metodo de la clase madre(la que hereda)

facundo = Ciudadano()
facundo.asignarNombre("Alen Facundo","Rios","Ñancucheo")

cody = CiudadanoNorteamericano()
cody.asignarNombre("Cody","Cocodrilo")

print(cody.nombreCompleto)
