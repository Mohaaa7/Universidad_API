import utils
from Semestres import Semestre

class SemestreDAO:
    def  __init__(self, db):
        self.__db = db

    def crear_semestre(self, semestre):
        with self.__db.cursor() as cursor:
            sql = "INSERT INTO semestre (nombre, idcarrera) VALUES (%s, %s)"
            cursor.execute(sql, (semestre.getNombre(), semestre.getIdCarrera()))
            self.__db.commit()
            return cursor.rowcount

    def actualizar_semestre(self, semestre):
        with self.__db.cursor() as cursor:
            sql = "UPDATE semestre SET nombre = %s, idcarrera = %s WHERE idsemestre = %s"
            cursor.execute(sql, (semestre.getNombre(), semestre.getIdCarrera(), semestre.getIdSemestre()))
            self.__db.commit()
            return cursor.rowcount

    def eliminar_semestre(self, semestre):
        with self.__db.cursor() as cursor:
            sql = "DELETE FROM semestre WHERE idsemestre = %s"
            cursor.execute(sql, (semestre.getIdSemestre(),))
            self.__db.commit()
            return cursor.rowcount

    def mostrar_semestres(self):
        with self.__db.cursor() as cursor:
            sql = "SELECT * FROM semestre"
            cursor.execute(sql)
            return cursor.fetchall()







          
            