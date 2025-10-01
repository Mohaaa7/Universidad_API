import utils

class Carrera: 
    def  __init__(self, db, cursor):
        self.__db = db
        self.__cursor = cursor

    def crear_carrera(self):
        nombre = input("Ingrese el nombre de la carrera: ")
        sql = "INSERT INTO carrera (nombre) VALUES (%s)"
        self.__cursor.execute(sql, (nombre,))
        self.__db.commit()
        print(f"Carrera creada: {nombre}")

    def actualizar_carrera(self):
        self.mostrar_carreras()
        id_carrera = int(input("Ingrese el ID de la carrera a actualizar: "))
        nuevo_nombre = input("Ingrese el nuevo nombre de la carrera: ")

        sql = "UPDATE carrera SET nombre = %s WHERE idcarrera = %s"
        self.__cursor.execute(sql, (nuevo_nombre, id_carrera))
        self.__db.commit()
        print(f"Carrera con ID {id_carrera} actualizada a: {nuevo_nombre}")

    def eliminar_carrera(self):
        self.mostrar_carreras()
        id_carrera = int(input("Ingrese el ID de la carrera a eliminar: "))

        sql = "DELETE FROM carrera WHERE idcarrera = %s"
        self.__cursor.execute(sql, (id_carrera,))
        self.__db.commit()
        print(f"Carrera con ID {id_carrera} eliminada.")

    def mostrar_carreras(self):
        sql = "SELECT * FROM carrera"
        self.__cursor.execute(sql)
        carreras = self.__cursor.fetchall()

        if carreras:
            print("\nCarreras registradas:")
            for id_carrera, nombre in carreras:
                print(f"   {id_carrera} - {nombre}")
        else:
            print("No hay carreras registradas.")


    def menu(self):
        opciones = {
            1: self.crear_carrera,
            2: self.actualizar_carrera,
            3: self.eliminar_carrera,
            4: self.mostrar_carreras
        }
        while True:
            opcion = utils.validar_numero(
                "Seleccione una Opcion:\n"\
                "   1.- Crear Carrera.\n"\
                "   2.- Actualizar Carrera.\n"\
                "   3.- Eliminar Carrera.\n"\
                "   4.- Mostrar Carreras Disponibles.\n"\
                "   0.- Volver.\n",
                0,4)
            if opcion == 0: return 
            accion = opciones.get(opcion)
            accion()