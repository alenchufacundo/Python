from tkinter import messagebox
from tkinter import *

def observacionImc(imc):
    resultados = ["BAJO PESO","NORMOPESO","SOBREPESO","OBESIDAD"]
    if (imc < 18.5):
        inputObservaciones.insert(0,resultados[0])
        inputObservaciones.config(bg="red")
    elif (imc >= 18.5 and imc <= 24.9):
        inputObservaciones.insert(0,resultados[1])
        inputObservaciones.config(bg="green")
    elif (imc > 24.9 and imc <= 29.5):
        inputObservaciones.insert(0,resultados[2])
        inputObservaciones.config(bg="yellow")
    else:
        inputObservaciones.insert(0,resultados[3])
        inputObservaciones.config(bg="red")

def comprobarStr(nombre):
    if nombre == "" or nombre == isdigit(nombre):
        messagebox.showerror(title="Error",message="Debes ingresar un nombre")

def comprobarNum(numero):
    if numero == "" or numero != isdigit(numero):
        messagebox.showerror(title="Error",message="Debes ingresar un numero")


def calcularImc():
    inputImc.delete(0,END)
    inputObservaciones.delete(0,END)
    peso = inputPeso.get()
    altura = inputAltura.get()
    nombre = inputNombre.get()
    edad = inputEdad.get()
    comprobarStr(nombre)
    comprobarNum(edad)
    comprobarNum(peso)
    comprobarNum(altura)
    try:
        resultadoImc = float(peso) / (float(altura) * float(altura))
    except:
        messagebox.showerror(title="Error",message="Debes ingresar un numero")
    else:
        inputImc.insert(0,round(resultadoImc,2))
        observacionImc(resultadoImc)

def borrarDatos():
    inputPeso.delete(0,END)
    inputEdad.delete(0,END)
    inputAltura.delete(0,END)
    inputNombre.delete(0,END)
    inputImc.delete(0,END)
    inputObservaciones.delete(0,END)


window = Tk()
window.title("Calculadora de IMC")
window.config(width=600,height=400)

labelNombre = Label(window,text="Nombre")
labelNombre.place(x=10,y=30)
inputNombre = Entry(window)
inputNombre.place(x=10,y=60)

labelEdad = Label(window,text="Edad")
labelEdad.place(x=10,y=90)
inputEdad = Entry(window)
inputEdad.place(x=10,y=120)

labelPeso = Label(window,text="Peso")
labelPeso.place(x=10,y=150)
inputPeso = Entry(window)
inputPeso.place(x=10,y=180)

labelAltura = Label(window,text="Altura")
labelAltura.place(x=10,y=210)
inputAltura = Entry(window)
inputAltura.place(x=10,y=240)

buttonCalcular = Button(window,text="CALCULAR IMC",command=calcularImc)
buttonCalcular.place(x=10,y=270)
buttonBorrar = Button(window,text="BORRAR",command=borrarDatos)
buttonBorrar.place(x=120,y=270)

labelImc = Label(window,text="IMC")
labelImc.place(x=10,y=300)
inputImc = Entry(window, text="")
inputImc.place(x=10,y=330)

labelObservaciones = Label(window,text="Observaciones")
labelObservaciones.place(x=270,y=300)
inputObservaciones = Entry(window,justify="center")
inputObservaciones.place(x=250,y=330)

window.mainloop()