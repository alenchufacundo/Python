from tkinter import *
import random

def generarNumAleatorio():
    numero = random.randint(0,99)
    numeroStr = str(numero)
    label.config(text=numeroStr)

vent = Tk()
vent.title("Numero Aleatorio")
vent.config(width=300,height=200)

#label
label = Label (vent,text="")
label.config(anchor="nw",bg="cyan",width=6,height=2,font=("Arial",30,"underline"))
label.place(x=70, y=10)

button = Button (vent,text="GENERAR", command=generarNumAleatorio)
button.config(bg="green")
button.place(x=110,y=140)




vent.mainloop()