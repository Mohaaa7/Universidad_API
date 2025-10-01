import mysql.connector 
from Carreras import Carrera
import utils

class DAOCarrera: 
    def  __init__(self, db):
        self.__db = db

    def crear_carrera(self, carrera):
        cursor = self.__db.cursor()
        sql = "INSERT INTO carrera (nombre) VALUES (%s)"
        cursor.execute(sql, (carrera.get_nombre(),))
        self.__db.commit()
        filas_modificadas = cursor.rowcount
        cursor.close()
        return filas_modificadas

    def actualizar_carrera(self, carrera):
        cursor = self.__db.cursor()
        sql = "UPDATE carrera SET nombre = %s WHERE idcarrera = %s"
        cursor.execute(sql, (carrera.get_nombre(), carrera.get_id()))
        self.__db.commit()
        filas_modificadas = cursor.rowcount
        cursor.close()
        return filas_modificadas

    def eliminar_carrera(self,carrera):
        cursor = self.__db.cursor()
        sql = "DELETE * FROM carrera WHERE idcarrera = %s"
        cursor.execute(sql, (carrera.get_id(),))
        self.__db.commit()
        filas_modificadas = cursor.rowcount
        cursor.close()
        return filas_modificadas

    def mostrar_carreras(self):
        cursor = self.__db.cursor()
        sql = "SELECT * FROM carrera"
        cursor.execute(sql)
        carreras = cursor.fetchall()
        cursor.close()
        return carreras