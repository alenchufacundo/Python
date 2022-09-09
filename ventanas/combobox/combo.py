#lista desplegable + entry es el combobox
#impoorta todas las librerias
from msilib.schema import ComboBox
from optparse import Values
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

def mostrarleng():
    l=cboLenguajes.get()#devuelve el elemento seleccionado en la lista desplegable
    pos=cboLenguajes.current()#devuelve la posicion del elemeento seleccionado en la lista desplegable
    print(l)
    print(pos)
    msg=f"usted selecciono el lenguaje {l}"
    messagebox.showinfo(title="Seleccion",message=msg)

ventana = Tk()
ventana.config(width=400,height=400)

et=Label(ventana,text="Seleccione el lenguaje") 
et.place(x=10,y=10)

leng = ["Python","Javascript","Ruby","Java","C++"]
cboLenguajes = ttk.Combobox(ventana, values=leng, width="9",state="readonly") #crea el combobox con 3 parametros 
                                                            #el state="readonly" es para que solamente se pueda leer y no escribir en el entry.
cboLenguajes.place(x=140,y=10)#los coloca

btn=Button(ventana,text="Seleccionar",command=mostrarleng)
btn.place(x=220,y=10)


ventana.mainloop()