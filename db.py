import mysql.connector

def crear_db(host="localhost", user="root", pwd="123456", db="moha_haroon"):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=pwd,
            database=db
        )
        print("Conexión establecida correctamente.")
        return mydb
    except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")
        return None
