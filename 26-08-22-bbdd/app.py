from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

colorBG = "beige"

def validation():
    try:
        connectSQL = sqlite3.connect("G:/26-08-22-bbdd/programa.db")
        cursor = connectSQL.cursor()
        user = entryUser.get()
        password = entryPassword.get()
        r = cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasenia = ?",(user,password))#esto son placeholder ?
        filas = r.fetchone() #selecciona el primero encontrado.
        if filas != None:
            messagebox.showinfo(title="Aviso",message="Acceso permitido")
            window2 = Toplevel() #toplevel -> crea una segunda ventana secundaria a la principal, sin necesidad de usar el mainloop().
            window2.config(width=600,height=600,bg=colorBG) #le define el tamanio a la altura.
            window.withdraw() #metodo para ocultar la ventana principal.

            # window.deiconify() este metodo sirve para mostrar nuevamente la ventana.
            # window.destroy() este metodo sirve para cerrar la ventana definivamente, la destruye.

        else:
            messagebox.showerror(title="Error",message="Acceso denegado, usuario o contraseña incorrecto")
    except sqlite3.OperationalError as error:
        print("error, no fue posible realizar la conexion a la base de datos")
        print(error)
    finally:
        connectSQL.close()
        print("Conexion finalizada")


window = Tk() 
window.title("Control de acceso")
window.config(width=300,height=400,bg=colorBG)

# resizeImage = imageUser.resize(width=20,height=20)
# imageUser = PhotoImage(resizeImage)
imageUser = PhotoImage(file="G:/26-08-22-bbdd/user.png")    
labelImage = Label(window,image=imageUser)
labelImage.place(x=90,y=20)


labelUser = Label(window,text="Usuario")
labelUser.config(width=20,height=2,bg=colorBG)
labelUser.place(x=70,y=120)
entryUser = Entry(window)
entryUser.config(width=10,font=("Impact",20))
entryUser.place(x=70,y=150)


labelPassword = Label(window,text="Contraseña")
labelPassword.config(width=20,height=2,bg=colorBG)
labelPassword.place(x=70,y=210)
entryPassword = Entry(window,show="*")
entryPassword.config(width=10,font=("Impact",20))
entryPassword.place(x=70,y=250)

buttonEnter = Button(window,text="Ingresar",bg="yellow",fg="black", command=validation)
buttonEnter.place(x=80,y=320)

buttonCancel = Button(window,text="Cancelar",bg="yellow",fg="black")
buttonCancel.place(x=150,y=320)

window.mainloop()