#controlar errores de codigo mediante conceptoes try/except -> es otra alteernativa de controlarloos mediante funciones caseras propias.

try: #en el try coloco la parte del codigo quepuede generar u error de ejecucion
    edad = int(input("Ingrese su edad: "))
except: #lo que quiero que haga si se genero un error
    print("edad erronea")
else:   #lo que quiero que se ejecute si no hay error.
    print("Su edad es:",edad)