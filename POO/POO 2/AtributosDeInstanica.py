#atributos de instancia

class Usuario:
    username = 'Facundo'
    email = ''

usuario1 = Usuario() #se instancia el objeto.
usuario1.email = 'alenfacurios@gmail.com'

print(usuario1.username)
print(usuario1.email)