from tkinter import *

def fgnegro():
    lbltexto.config(fg="Black")

def fgrojo():
    lbltexto.config(fg="red")

def fgazul():
    lbltexto.config(fg="blue")

def fgverde():
    lbltexto.config(fg="green")

def fgnaranja():
    lbltexto.config(fg="orange")

def fontarial():
    lbltexto.config(font=("Arial",30,"bold"))

def fontimpact():
    lbltexto.config(font=("Impact",30,"bold"))

def fontlucida():
    lbltexto.config(font=("Lucida Console",30,"bold"))

def cambiartexto():
    t=txttexto.get()#obtiene lo ingresado en un entry y lo guarda en la variable t
    lbltexto.config(text=t)

win=Tk()
win.title("Segunda aplicacion")
win.config(width=400,height=400)
win.resizable(0,0)
win.config(bg="#DD5F44")

lbltexto=Label(win,text="HOLA")
lbltexto.config(font=("Arial", 30))
lbltexto.config(width=15,height=2)
lbltexto.place(x=25,y=10)

lblcolor=Label(win,text="Foreground:")
lblcolor.config(bg="#DD5F44")
lblcolor.place(x=25,y=120)

btnnegro=Button(win,text="Negro")
btnnegro.config(width=10,height=1)
btnnegro.config(command=fgnegro)
btnnegro.place(x=25,y=140)

btnrojo=Button(win,text="Rojo")
btnrojo.config(width=10,height=1)
btnrojo.config(command=fgrojo)
btnrojo.place(x=25,y=170)

btnazul=Button(win,text="Azul",command=fgazul)
btnazul.config(width=10,height=1)
btnazul.place(x=25,y=200)

btnverde=Button(win,text="Verde",command=fgverde)
btnverde.config(width=10,height=1)
btnverde.place(x=25,y=230)

btnnaranja=Button(win,text="Naranja",command=fgnaranja)
btnnaranja.config(width=10,height=1)
btnnaranja.place(x=25,y=260)

btnarial=Button(win,text="Arial",command=fontarial)
btnarial.config(width=10,height=1)
btnarial.place(x=25,y=310)

btnimpact=Button(win,text="Impact",command=fontimpact)
btnimpact.config(width=10,height=1)
btnimpact.place(x=25,y=340)

btnlucida=Button(win,text="Lucida Console",command=fontlucida)
btnlucida.config(width=10,height=1)
btnlucida.place(x=25,y=370)

lbl=Label(win,text="Ingrese texto:")
lbl.config(bg="#DD5F44")
lbl.place(x=270,y=120)

txttexto=Entry(win)
txttexto.config(width=15)
txttexto.place(x=270,y=140)

btncambiar=Button(win,text=">",command=cambiartexto, cursor="pencil")
btncambiar.config(width=3,height=1)
btncambiar.place(x=365,y=135)

win.mainloop()