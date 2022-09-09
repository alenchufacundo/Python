import pymysql

#crea otra constante con la sentencia sql de eliminar la tabla users si existe.
DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

#crea una constante con las sentencia SQL, #string de triple comillas es para que se pueda hacer un string de muchas lineas
USERS_TABLE = """
    CREATE TABLE users(
        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL, 
        email VARCHAR(50) NOT NULL, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""

#conexion a base de datos
if __name__ == '__main__': #esta linea nos permite saber si un script esta siendo importado o ejecutado si mismo, es decir que no es importado.
    #PREGUNTA si es el archivo main. Es main si el script no es importado.
    try:
        connectMySql = pymysql.Connect(host = 'localhost', #crea una variables con la conexion a la base de datos.(un objeto crea de tipo connect)
                        port = 3306,
                        user = 'root',
                        passwd = 'kapo.10.alen',  #es la contraseña que puse al instalar mysql.
                        db = 'pythondb'
                        )
        

        with connectMySql.cursor() as cursor:
            # cursor = connectMySql.cursor() #crea un objeto de tipo cursor que nos permite ejecutar las sentencias SQL sobre la base de datos.(un objeto crea de tipo)
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE) #execute(variable con sentencias SQL) ejecuta las sentencias SQL.
            print('conexion exitosa')
    except pymysql.err.OperationalError as errorBd: #agrega el error que salio antes y lo define como err.
        print('error, no fue posible realizar la conexion')
        print(errorBd)

    finally: #metodo finally se ejecuta cuando se hace el try o el except. Es el bloque clasula.
        #finaliza el cursor y la conexion mysql
        # cursor.close()
        connectMySql.close()
        print("conexion finalizada")

