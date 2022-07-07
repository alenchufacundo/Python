from tkinter import Tk, messagebox, simpledialog

window = Tk()
window.withdraw()

#simpledialog.askinteger/float/string -> es para pedir datos.
edad = simpledialog.askinteger(title="Datos",prompt="Ingrese su edad: ",parent=window)
msg = "Su edad es " + str(edad) +" años"
#str() pasa el entero a string, usar el + para concantenar y no aparezca llaves en el box. Si usas , aparecen {}
if (edad == None):
    messagebox.showerror(title="Error",message="No ingreso ningún número")
else:
    messagebox.showinfo(title="Informacion",message=msg)
