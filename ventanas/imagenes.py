from tkinter import *

def cambiarImagen ():
    if f[0] == True: #se uso una lista/array como bandera, ya que sin lista no funciona la logica
        l.config(image = imagen)
        f[0] = False
        print(f)
    else:
        l.config(image = imagen2)
        f[0] = True
        print(f)

app = Tk ()
f = [True] #usar lista para poder usarse dentro de una funcion
app.config(width=400, height=300)
imagen = PhotoImage(file="ventanas/imagenes/boca2.png")
l = Label(app, image = imagen)
l.place (x = 10, y = 10)
imagen2 = PhotoImage(file="ventanas/imagenes/river.png")
button = Button(app,text="Cambiar",command=cambiarImagen)
button.place(x=300,y=250)

app.mainloop()
