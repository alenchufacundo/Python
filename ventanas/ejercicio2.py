from tkinter import Tk, messagebox, simpledialog
from random import randint
from ejercicio1 import comprobarNumero

window = Tk()
window.withdraw()

#funciones
#def comprobarNumero (numero):
#    if (numero == None):
#        messagebox.showerror(title="Error",message="No ingreso ningun numero")
#    else:
#        return numero  

def generarNumAleatorio(numero1, numero2):
    if numero1 < numero2:
        numeroAleatorio = randint(numero1, numero2)
    else:
        numeroAleatorio = randint(numero2, numero1)
    messagebox.showinfo(title="Numero aleatorio", message=numeroAleatorio)

def comprobarIgualdadNum(numero1, numero2):
    if numero1 == numero2:
        messagebox.showinfo(title="Error",message="Debes colocar 2 numeros diferentes")
        return True
    else:
        return False

def pedirDatos():
    counter = 0
    while (counter == 0):
        numero1 = simpledialog.askinteger(title="Datos",prompt="Ingrese un numero: ", parent=window)
        numero2 = simpledialog.askinteger(title="Datos",prompt="Ingrese un numero: ", parent=window)
        if (comprobarNumero(numero1)) and (comprobarNumero(numero2)) and (not comprobarIgualdadNum(numero1,numero2)):#not es lo mismo que ! ->negacion.
            counter += 1
            return numero1, numero2

#ejecucion programa
numeros = pedirDatos() #esto siempre devuelve una tupla
generarNumAleatorio(numeros[0],numeros[1])

