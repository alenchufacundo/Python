from tkinter import *

def cambiarcolor():
    app.config(bg="VioletRed4")

app=Tk()
app.title("REPASO")
app.config(width=450,height=450,bg="NavajoWhite3")

L=Label(app,text="Mensaje en pantalla:")
L.config(width=20,height=2,fg="SeaGreen3")
L.place(x=30,y=30)

B=Button(app,text="Click AQUI",command=cambiarcolor)
B.config(width=14,height=3)
B.place(x=30,y=70)

E=Entry(app)
E.config(width=17,bg="SteelBlue3",fg="white")
E.config(font=("Impact",20,"italic"))
E.place(x=30,y=130)

ima=PhotoImage(file="..\ventanas\imagenes\river.jpg")
LB=Label(app,image=ima)
#LB.config(width=250,height=250)
LB.place(x=10,y=170)

ima2=PhotoImage(file="..\ventanas\imagenes\river")
LB2=Label(app,image=ima2)
LB2.place(x=220,y=170)
app.mainloop()