import sqlite3

if __name__ == '__main__':

    try:
        connectSQL = sqlite3.connect("G:/26-08-22-bbdd/programa.db")
        cursor = connectSQL.cursor()

    except sqlite3.OperationalError as error:
        print("error, no fue posible realizar la conexion a la base de datos")

    finally:
        connectSQL.close()
        print("Conexion finalizada")

