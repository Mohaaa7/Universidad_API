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

def iniciar_sesion():
    while True:
        user = input("Introduzca su nombre de usuario: ")
        pwd = input("Introduzca su contraseña: ")
        db = crear_db("localhost", user, pwd, "moha_haroon")
        if db:
            return db
        else:
            print("Intente nuevamente.\n")
            opcion = input("¿Desea volver a intentar? (s/n): ").strip().lower()
            if opcion != "s":
                exit()