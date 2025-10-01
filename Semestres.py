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

    def actualizar_semestre(self):
        self.mostrar_semestres()
        id_semestre = utils.validar_numero("Ingrese el ID del semestre a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del semestre: ")
        nuevo_id_carrera = utils.validar_numero("Ingrese el nuevo id de la carrera: ")

        sql = "UPDATE semestre SET nombre = %s, idcarrera = %s WHERE idsemestre = %s"
        self.__cursor.execute(sql, (nuevo_nombre, nuevo_id_carrera, id_semestre))
        self.__db.commit()
        if self.__cursor.rowcount == 0:
            print("No se ha podido actualizar")
        else:
            print(f"Semestre con ID {id_semestre} actualizada")

    def mostrar_semestres():
        pass