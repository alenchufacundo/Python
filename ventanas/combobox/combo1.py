from msilib.schema import ComboBox
from optparse import Values
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def cambiarcolor():
    color=cbocolores.current()
    if color==0:
        ventana.config(bg="Black")
    if color==1:
        ventana.config(bg="red")
    if color==2:
        ventana.config(bg="blue")
    if color==3:
        ventana.config(bg="green")
    if color==4:
        ventana.config(bg="Orange")
    if color==5:
        ventana.config(bg="pink")
    if color==6:
        ventana.config(bg="yellow")
    

ventana=Tk()
ventana.config(width=400,height=400)

et=Label(ventana,text="Seleccione color:")
et.place(x=10,y=10)

colores=["Negro","Rojo","Azul","Verde","Naranja","Rosa","Amarillo"] #crea la lista deopciones que van a verse en el combobox
cbocolores=ttk.Combobox(ventana,values=colores,width="10",state="readonly")#crea el combobox y lo conecta con la lista
cbocolores.place(x=130,y=10)

btnaplicar=Button(ventana,text="Aplicar",width=10,command=cambiarcolor)
btnaplicar.place(x=250,y=10)


ventana.mainloop()