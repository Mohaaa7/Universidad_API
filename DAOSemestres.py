import utils
from Semestres import Semestre

class DAOSemestre:
    
    # Constructor
    def  __init__(self, db):
        self.__db = db

    # Método para crear semestres
    def crear_semestre(self, semestre):
        with self.__db.cursor() as cursor:
            sql = "INSERT INTO semestre (nombre, idcarrera) VALUES (%s, %s)"
            cursor.execute(sql, (semestre.getNombre(), semestre.getIdCarrera()))
            self.__db.commit()
            return cursor.rowcount

    # Método para actualizar semestres
    def actualizar_semestre(self, semestre):
        with self.__db.cursor() as cursor:
            sql = "UPDATE semestre SET nombre = %s, idcarrera = %s WHERE idsemestre = %s"
            cursor.execute(sql, (semestre.getNombre(), semestre.getIdCarrera(), semestre.getIdSemestre()))
            self.__db.commit()
            return cursor.rowcount

    # Método para eliminar semestres
    def eliminar_semestre(self, semestre):
        with self.__db.cursor() as cursor:
            sql = "DELETE FROM semestre WHERE idsemestre = %s"
            cursor.execute(sql, (semestre.getIdSemestre(),))
            self.__db.commit()
            return cursor.rowcount

    # Método para mostrar semestres
    def mostrar_semestres(self):
        with self.__db.cursor() as cursor:
            sql = """
                SELECT s.idsemestre, s.nombre AS nombre_semestre, 
                       c.idcarrera, c.nombre AS nombre_carrera
                FROM semestre s
                INNER JOIN carrera c ON s.idcarrera = c.idcarrera
            """
            cursor.execute(sql)
            return cursor.fetchall()








