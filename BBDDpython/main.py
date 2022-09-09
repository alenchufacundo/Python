import pymysql
from decouple import config


DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLE = """
    CREATE TABLE users(
        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL, 
        email VARCHAR(50) NOT NULL, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""

#crea una variable de tipo lista donde la misma almacena tuplas. importante para insertas multiples registros.
usersInsertar = [
    ("user1","password","user1@gmail.com"),
    ("user2","password","user2@gmail.com"),
    ("user3","password","user3@gmail.com"),
    ("user4","password","user4@gmail.com"),
]

#conexion a base de datos
if __name__ == '__main__':

    try:
        connectMySql = pymysql.Connect(host = 'localhost',
                        port = int(config('PORT_MYSQL')), #importante convertirlo a integer, porque toma el '3306' como string
                        user = config('USER_MYSQL'), #variable de entorno con el config('variableDeEntorno')
                        passwd = config('PASSWORD_MYSQL'), #variable de entorno con el config('variableDeEntorno')
                        db = config('DB_MYSQL') #variable de entorno con el config('variableDeEntorno')
                        )
        

        with connectMySql.cursor() as cursor:
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)

            #--------------------------------------------------------------
            #INSERTAR REGISTROS
            #--------------------------------------------------------------

            #query para insertar registros
            queryInsertar = "INSERT INTO users(username,password,email) VALUES(%s, %s, %s)" #%s son placeholders, es decir esta como algo pasajero, despues es reemplazado por los values.
            # values = ("alenchu","6338","alenfacurios@gmail.com") #esto es una tupla.

            #ciclo foreach que recorre los elementos de la lista de users.
            # for user in usersInsert:
            #     cursor.execute(queryInsertar,user)

            #otro metodo alternativo: cursor.executemany() este metodo nos permite ejecutar multiples sentencias
            cursor.executemany(queryInsertar,usersInsertar)
            connectMySql.commit()

            #--------------------------------------------------------------
            #OBTENER REGISTROS
            #--------------------------------------------------------------

            #obtener registros de la tabla users
            # queryObtener = "SELECT * FROM users"
            # rows = cursor.execute(queryObtener) #execute retorna la cantidad de filas o registros que se obtienen y lo almacena en una variable.

            #metodo objeto/variable.fetchall()
            # for user in cursor.fetchmany(1): #este metodo nos retorna una tupla dentro de otra tupla con todos los registros de la queryObtener declarada
            #     print(user)

            #--------------------------------------------------------------
            ##ACTUALIZAR REGISTROS
            #--------------------------------------------------------------

            # queryActualizar = "UPDATE users SET username=%s WHERE id=%s" #otra vez usa placeholders %s
            # valuesActualizar =  ("nuevoUsername", 1) #los values tiene que ir en una tupla

            # cursor.execute(queryActualizar,valuesActualizar)
            # connectMySql.commit()

            #--------------------------------------------------------------
            #ELIMINAR REGISTROS
            #--------------------------------------------------------------

            queryEliminar = "DELETE FROM users WHERE id=%s" #otra vez usa placeholders %s
            valuesEliminar = (2)
            
            cursor.execute(queryEliminar,valuesEliminar)
            connectMySql.commit()


            print('conexion exitosa')

            
    except pymysql.err.OperationalError as errorBd:
        print('error, no fue posible realizar la conexion')
        print(errorBd)

    finally:
        connectMySql.close()
        print("conexion finalizada")

