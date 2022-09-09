class Usuario:
    def __init__(self,dni): #se ejecuta cuando se instancia un objeto
        self.username = 'facundo'
        self.password = ''
        self.dni = dni

user1 = Usuario(39877510)#parametro dni que puse arriba.
print(user1.dni)
