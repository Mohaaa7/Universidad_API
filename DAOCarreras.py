class DAOCarrera: 
    def  __init__(self, db):
        self.__db = db

    def crear_carrera(self, carrera):
        with self.__db.cursor() as cursor:
            sql = "INSERT INTO carrera (nombre) VALUES (%s)"
            cursor.execute(sql, (carrera.get_nombre(),))
            self.__db.commit()
            return cursor.rowcount

    def actualizar_carrera(self, carrera):
        with self.__db.cursor() as cursor:
            sql = "UPDATE carrera SET nombre = %s WHERE idcarrera = %s"
            cursor.execute(sql, (carrera.get_nombre(), carrera.get_id()))
            self.__db.commit()  
            return cursor.rowcount

    def eliminar_carrera(self,carrera):
        with self.__db.cursor() as cursor:
            sql = "DELETE FROM carrera WHERE idcarrera = %s"
            cursor.execute(sql, (carrera.get_id(),))
            self.__db.commit()
            return cursor.rowcount

    def get_carreras(self):
        with self.__db.cursor() as cursor:
            sql = "SELECT * FROM carrera"
            cursor.execute(sql)
            return cursor.fetchall()
        
