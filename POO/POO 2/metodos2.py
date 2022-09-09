class Usuario:
    def inicializar(self,nombre,pw):
        self.username = nombre
        self.password = pw
user1 = Usuario()
user2 = Usuario()
user1.inicializar('Alen', '6338') #se llama al metodo inicializar que lo que hace es agregar los atributos.
print(user1.password)
print(user1.username)
