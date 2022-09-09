from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def mostrar():
    try:
        currentSelection = lista.get(lista.curselection()) #necesario seleccionar un elemento para que devuelva el valor
    except:
        messagebox.showerror(title="Error",message="Debes seleccionar una opcion")
    finally:
        msg = f"Usted selecciono {currentSelection}"
        messagebox.showinfo(title="Info",message=msg)
        print(currentSelection)

def eliminar():
    try:
       currentSelection = lista.curselection()
    except:
        messagebox.showerror(title="Error",message="Debes seleccionar una opcion")
    finally:
        lista.delete(currentSelection)
        msg=f"Usted elimino el dia seleccionado"
        messagebox.showinfo(title="Info",message=msg)
        
def modificar():
    pass 



ventana = Tk()
lista = Listbox(ventana, width=10,height=10)#crea una lista tipo lista, sin entry
lista.place(x=30,y=40)
lista.insert(0,"Lunes")
lista.insert(1,"Martes")
lista.insert(2,"Miercoles","Jueves","Viernes")
lista.insert(END, "Sabado")#variable end, indica final del array. 
print(lista.size())
lista.delete(1)
boton = Button(ventana,text="Presionar",command=mostrar)
boton.place(x=100,y=35)

boton1 = Button(ventana,text="Eliminar",command=eliminar)
boton1.place(x=100,y=70)

boton2 = Button(ventana,text="Presionar",command=modificar)
boton2.place(x=100,y=105)

ventana.mainloop()