from tkinter import *
from tkinter import messagebox

def calcularsuma():
    n1=txtnro1.get()
    n2=txtnro2.get()
    try:
        r=int(n1)+int(n2)
    except:
        messagebox.showerror(title="ERROR",message="Debe ingresar valores enteros!!")
    else:
        lblres2.config(text=r)

def borrardatos():
    txtnro1.delete(0,END)
    txtnro2.delete(0,END)
    lblres2.config(text="")

vent=Tk()
vent.title("Sumador")
vent.config(width=300,height=300)

lbl1=Label(vent,text="Ingrese primer numero:")
lbl1.place(x=10,y=10)

txtnro1=Entry(vent)
txtnro1.place(x=10,y=30)

lbl2=Label(vent,text="Ingrese segundo numero:")
lbl2.place(x=10,y=60)

txtnro2=Entry(vent)
txtnro2.place(x=10,y=80)

lblres=Label(vent,text="Resultado")
lblres.place(x=200,y=10)

lblres2=Label(vent,text="0",font=("Arial Black",50))
lblres2.place(x=200,y=30)

btncalcular=Button(vent,text="CALCULAR",command=calcularsuma)
btncalcular.place(x=10,y=110)

btnborrar=Button(vent,text="BORRAR",command=borrardatos)
btnborrar.place(x=90,y=110)


vent.mainloop()