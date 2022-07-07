from tkinter import Tk, messagebox, simpledialog
#importa libreria que trae ventanas de dialogo(windows)

#aparece una ventana chiquita
ventana = Tk() #crea una ventana Tk()
ventana.withdraw()#oculta ventana
messagebox.showinfo(title="saludo",message="bienvenido")
messagebox.showwarning(title="Advertencia",message="Ingrese un numero correcto")
messagebox.showerror(title="Error",message="error en la validacion")
