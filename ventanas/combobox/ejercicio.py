from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from wsgiref.validate import InputWrapper

def obtenerImporte():
    importe = float(entryImporte.get())
    return importe

def obtenerOpcion():
    currentSelection = listaFormasPago.curselection()
    return currentSelection

def calcular():
    importe = obtenerImporte()
    currentSelection = obtenerOpcion()
    print(currentSelection[0])
    if listaFormasPago[currentSelection[0]] == listaFormasPago[0]:
        resultadoTotal = importe * 0.95
        resultadoEntry.insert(0,resultadoTotal)


window = Tk()
window.config(width=350,height=300,bg="gray")

importe = Label (window)
importe.config(anchor="center",bg="gray",text="IMPORTE",width=8,height=1,font=("Arial",9))
importe.place(x=10, y=15,)

entryImporte = Entry(window)
entryImporte.config(width=10)
entryImporte.place(x=80,y=15)

formasPago = Label(window)
formasPago.config(anchor="center",bg="gray",text="FORMAS DE PAGO",width=16,height=1,font=("Arial",9))
formasPago.place(x=9, y=60)

listaFormasPago = Listbox(window,width=25,height=4)
listaFormasPago.place(x=130,y=60)
listaFormasPago.insert(END, "EFECTIVO: desc 5%","CREDITO 1 cuota: desc 8%","CREDITO 3 cuota: desc 15%","CREDITO 6 cuota: desc 28%")

botonCalcular = Button(window,text="Calcular",command=calcular)
botonCalcular.place(x=15,y=150)

resultadoEntry = Entry(window,width=15)
resultadoEntry.place(x=15,y=190)


window.mainloop()