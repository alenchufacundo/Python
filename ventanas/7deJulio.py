from tkinter import *

win=Tk()
win.title("Segunda aplicacion")
win.config(width=400,height=400)
win.resizable(0,0)
win.config(bg="#DD5F44")

lblnombre=Label(win,text="Christian Coria")
lblnombre.place(x=50,y=30)
lblnombre.config(bg="#DD5F44")#background
lblnombre.config(fg="red")#foreground

lbldni=Label(win,text="DNI: 23.245.964")
lbldni.place(x=50,y=50)
lbldni.config(bg="#DD5F44",fg="blue")

btnaceptar=Button(win,text="Aceptar") 
btnaceptar.config(width=10,height=2)
btnaceptar.config(bg="#CD80F5")
btnaceptar.place(x=150,y=40)

txtmsj=Entry(win)
txtmsj.config(width=25,bg="#F1F6A0",fg="blue")
txtmsj.place(x=50,y=100)

win.mainloop()