import utils
from Semestres import Semestre

class SemestreDAO:
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

    def eliminar_semestre(self):
        self.mostrar_semestres()
        id_semestre = utils.validar_numero("Ingrese el ID del semestre a eliminar: ")

        sql = "DELETE FROM semestre WHERE idsemestre = %s"
        self.__cursor.execute(sql, (id_semestre,))
        self.__db.commit()
        if self.__cursor.rowcount == 0:
            print("No se ha podido eliminar")
        else:
            print(f"Semestre con ID {id_semestre} eliminada.")

    def mostrar_semestres(self):
        sql = "SELECT * FROM semestre"
        self.__cursor.execute(sql)
        semestres = self.__cursor.fetchall()

        if semestres:
            print("\Semestres registrados:")
            print("   ID - Nombre")
            for idSemestre, nombre in semestres:
                print(f"   {idSemestre} - {nombre}")
        else:
            print("No hay semestres registrados.")

    def menu(self):
        opciones = {
            1: self.crear_semestre,
            2: self.actualizar_semestre,
            3: self.eliminar_semestre,
            4: self.mostrar_semestres
        }
        while True:
            opcion = utils.validar_numero(
                "Seleccione una Opcion:\n"\
                "   1.- Crear Semestre.\n"\
                "   2.- Actualizar Semestre.\n"\
                "   3.- Eliminar Semestre.\n"\
                "   4.- Mostrar Semestres Disponibles.\n"\
                "   0.- Volver.\n",
                0,4)
            if opcion == 0: return 
            accion = opciones.get(opcion)
            accion()






            