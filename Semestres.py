import utils

class Semestre:
    def  __init__(self, db, cursor):
        self.__db = db
        self.__cursor = cursor

    def crear_semestre(self):
        nombre = input("Ingrese el nombre del semestre: ")
        id_carrera = input("Ingrese el id de la carrera: ")
        sql = "INSERT INTO semestre (nombre, idSemestre) VALUES (%s, %s)"
        self.__cursor.execute(sql, (nombre, id_carrera))
        self.__db.commit()
        print(f"Semestre creado: {nombre}")

    