from tkinter import *
window = Tk()
window.title ("Bienvenido mundo") #pone el titulo
#window.geometry("800x600") #define el tamaño de la ventana.
window.config(width = 800, height= 600)#define medidas al igual que el geometry
window.config(bg = "#E7D40A") #cambia el color del background
window.resizable(1000,1000) #metodo que hace que la ventana de windows no puede ajustarse o adjustarlo a una manera determinada
etiqueta1 = Label(window,text="nombre")#crea una etiqueta(ventana donde quiero que aparezca, texto que quiero que aparezca)
#etiqueta1.pack() #ejecuta el labe y los coloca uno abajo del otro6
etiqueta1.place(x = 80, y = 120)#define la posicion del label -> (eje x, eje y)
etiqueta1.config(width=10, height=5, bg="#109DFA", fg="#EF280F")
button = Button(window,text="click aca",bg="pink")#inserta boton
button.place(width=60, height=30, x=85, y = 240)
caja = Entry(window)#crea un textfield o textarea
caja.place(x = 50, y = 190)
window.mainloop ()