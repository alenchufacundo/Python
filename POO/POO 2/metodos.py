class Usuario:
    def inicializar(self):
        self.username = 'Facundo'
        self.password = '123'

user1 = Usuario()
user2 = Usuario()
user1.inicializar() #se llama al metodo inicializar que lo que hace es agregar los atributos.
print(user1.password)

        
