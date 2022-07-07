class PlanCurricular:
    def __init__(self,nombre): #parametro nombre
        self.nombre = nombre


class Bootcamp(PlanCurricular):
    def __init__(self,nombre,nombreBootcamp):
        super().__init__(nombre) #se utiliza el super para llamar al constructor de la clase madre/padre -> ya que si no, se sobreeesribe y tira error.
        self.nombreBootcamp = nombreBootcamp

    def inscribir(self):
        print("hola",self.nombre,",bievenido al bootcamp")

nuevoPlan = Bootcamp("Martin","Introduccion") #se le pasa el parametro del constructor de la clase madre
nuevoPlan.inscribir()

