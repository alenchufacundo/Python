import sqlite3


SELECT = "SELECT * FROM cursos"

if __name__ == '__main__':

    try:
        connectSQL = sqlite3.connect("G:\BBDDpython\SQLite\cfp.db")
    
        cursor = connectSQL.cursor()

        # insertar registros
        # values = (5,"carpitenria","domingos","15","18")
        # queryInsert = "INSERT INTO cursos(id,nombrecurso,dias,horainicio,horafin) VALUES(?,?,?,?,?)"+values
        # cursor.execute(queryInsert)
        # connectSQL.commit()

        # queryEliminar = "DELETE FROM cursos WHERE id = 4"
        # cursor.execute(queryEliminar)
        # connectSQL.commit()

        # #consultar registros
        # fields = cursor.execute(SELECT)
        # for element in fields:
        #     print(element)


    except:
        print("conexion erronea")
    finally:
        connectSQL.close()
        print("conexion finalizada")

