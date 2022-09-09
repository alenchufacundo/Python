from tkinter import *
from tkinter import ttk
import pymysql


def editWindow():
    editWindow = Toplevel()
    # editWindow = Tk()
    editWindow.title("Editor de preguntas y respuestas")
    editWindow.config(width=800,height=600)

    # labelTitle = Label(editWindow,text="Proximamente podras agregar, editar y eliminar preguntas/respuestas")
    # labelTitle.place(x=100,y=50)
    labelTitle = Label(editWindow,text="Editor de preguntas y respuestas",font=("Arial",15,"bold"))
    labelTitle.place(x=50,y=50)

    try:
        connect = pymysql.connect(
            host = "localhost",
            port = 3306,
            user = "rootafr",
            password = '6338.hola',
            db = "preguntados"
        )
        with connect.cursor() as cursor:
            query = "SELECT * FROM preguntados"
            cursor.execute(query)
            rows = cursor.fetchall()
            preguntas = []
            for row in rows:
                idOpcion,pregunta,opcion1,opcion2,opcion3,opcion4,resultado = row
                preguntas.append(pregunta)
            print(preguntas)

            listaPreguntas = ttk.Combobox(editWindow,values=preguntas,width="70",state="readonly")
            listaPreguntas.place(x=50,y=100)

            buttonUpdate = Button(editWindow,text="Actualizar")
            buttonUpdate.place(x=520,y=95)
            buttonDelete = Button(editWindow,text="Borrar")
            buttonDelete.place(x=600,y=95)
            buttonCreate = Button(editWindow,text="Crear")
            buttonCreate.place(x=660,y=95)

            opciones = [opcion1,opcion2,opcion3,opcion4]

    except pymysql.err.OperationalError as error:
        print(error)
        print("error, no fue posible realizar la conexion a la base de datos")
    finally:
        connect.close()
        print("conexion finalizada.")


# editWindow.mainloop()