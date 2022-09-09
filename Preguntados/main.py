from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from exitDef import *
from tkinter import ttk
import PIL.Image
from gameApp import *
from editApp import *

window= Tk()
window.title("Juego de preguntas y respuestas")
window.config(width=650,height=400)
window.resizable(0,0)

# Resizing image
imageLogo = PIL.Image.open("Preguntados/images/logo.png")
imageLogo = imageLogo.resize((100,80))
newImage = ImageTk.PhotoImage(imageLogo)
labelImage = Label(image=newImage)
labelImage.place(x=270,y=40)

#Inicio
btnInicio  = Button(window,text="Inicio",command=lambda:mainGame(window))
btnInicio.config(width=15,height=2)
btnInicio.place(x=260,y=150)

#Agregar preguntas
btnAgregar  = Button(window,text="Editar", command=editWindow)
btnAgregar.config(width=15,height=2)
btnAgregar.place(x=260,y=210)

#Salir juego
btnAgregar  = Button(window,text="Salir", command=lambda:salirJuego(window))
btnAgregar.config(width=15,height=2)
btnAgregar.place(x=260,y=270)


window.mainloop() 