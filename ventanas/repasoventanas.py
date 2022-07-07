from tkinter import Tk,messagebox, simpledialog

ventana = Tk()
ventana.withdraw ()
respuesta = messagebox.askretrycancel(title="borrar",message="Esta seguro que desea borra el cliente?")
if (respuesta == True):
    print("confirmo eliminacion")
else:
    print("denego eliminacion")

ventana.mainloop ()#muestra la pantalla en ventana

 