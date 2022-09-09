from tkinter import *

def mostrarboca():
    L.config(image=imaboca)

def mostrarriver():
    L.config(image=imariver)

app=Tk()
app.title("BOCA-RIVER")
app.config(width=400,height=400,bg="NavajoWhite3")

imaboca=PhotoImage(file="boca.gif")
imariver=PhotoImage(file="river.gif")

B1=Button(app,text="Ver BOCA",command=mostrarboca)
B1.config(width=20,height=3)
B1.place(x=30,y=30)

B2=Button(app,text="Ver RIVER",command=mostrarriver)
B2.config(width=20,height=3)
B2.place(x=220,y=30)

L=Label(app)
L.config(bg="NavajoWhite3")
L.place(x=100,y=150)



app.mainloop()