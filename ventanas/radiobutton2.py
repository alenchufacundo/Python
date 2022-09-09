from tkinter import *
from tkinter import messagebox

def calcular ():
    if operacion == 1:
        numero1 = e1.get()
        numero2 = e2.get()
        try:
            resultadoSuma = int(numero1) + int(numero2)
        except:
            messagebox.showerror(title="Error",message="Debes ingresar un numero")
        else:
            resultadoEntry.insert(0,resultadoSuma)
    if operacion == 2:  
        numero1 = e1.get()
        numero2 = e2.get()
        try:
            resultadoResta = int(numero1) - int(numero2)
        except:
            messagebox.showerror(title="Error",message="Debes ingresar un numero")
        else:
            resultadoEntry.insert(0,resultadoResta)

    

app = Tk()#esto va primero
operacion = IntVar() #integer variable
operacion.set(1) #setea en 1 el value de operacion
app.title("Calculadora")
app.config(width = 400, height=600)
l1 = Label(app, text="Numero 1")
l1.place(x=5, y=5)
e1 = Entry(app)
e1.config(width= 6)
e1.place(x=5,y=35)

l2 = Label(app, text="Numero 2")
l2.place(x=5, y=60)
e2 = Entry(app)
e2.config(width= 6)
e2.place(x=5,y=90)

opcion = Label(app,text="Seleccione operacion")
opcion.place(x= 200,y=5)

rbs = Radiobutton(app,text="Suma", value=1, variable=operacion)
rbs.place(x=220,y = 30)
rbr = Radiobutton(app,text="Resta", value=2, variable=operacion)
rbr.place(x=220,y = 60)
rbd = Radiobutton(app,text="Division", value=3, variable=operacion)
rbd.place(x=220,y = 90)
rbm = Radiobutton(app,text="Multiplicacion", value=4, variable=operacion)
rbm.place(x=220,y = 120)


button = Button(app, text="CALCULAR",command=calcular)
button.config(width=10,height=1)
button.place(x = 5, y = 130)

button2 = Button(app, text="BORRAR")
button2.config(width=10,height=1)
button2.place(x = 100, y = 130)

resultadoLabel = Label(app,text="Resultado")
resultadoLabel.place(x = 80, y= 180)
resultadoEntry = Entry(app, text="Resultado")
resultadoEntry.config(width=15)
resultadoEntry.place(x = 60, y =200)

app.mainloop()