from tkinter import Tk, messagebox, simpledialog

window = Tk()
window.withdraw

#definicion de funciones

def comprobarNumero (numero):
    if (numero == None):
        messagebox.showerror(title="Error",message="No ingreso ningun numero")
    else:
        return numero  

def pedirPrecio(): 
    counter = 0
    while counter == 0:
        precio = simpledialog.askfloat(title="PRECIO", prompt="Ingrese un precio",parent=window)
        if (comprobarNumero(precio)):
            return precio
            counter +=1

def calcularPorcentaje (precio):
    porcentaje = 13
    porcentaje = (precio * 13) / 100
    msg = "El 13% de "+str(precio)+" es "+str(porcentaje)
    messagebox.showinfo(title = "Porcentaje",message = msg)

#ejecucion del programa
#precio = pedirPrecio()
#calcularPorcentaje(precio)
