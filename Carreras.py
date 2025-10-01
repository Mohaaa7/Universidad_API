import utils

class Carrera: 
    def  __init__(self, db, cursor):
        #self.__db = db
        #self.__cursor = cursor
        ""

    def crear_carrera(self):
        nombre = input("Ingrese el nombre de la carrera: ")
        sql = "insert into carrera (nombre) values (%s)"
        """
        self.__cursor.execute(sql, nombre)
        self.__db.commit()
        """
        print(f"Creacion de carrera: {nombre}")

    def actualizar_carrera(self):
        print("Logica de actualizar_carrera")
    def eliminar_carrera(self):
        print("Logica de eliminar_carrera")
    def mostrar_carreras(self):
        print("Logica de mostrar_carreras")

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