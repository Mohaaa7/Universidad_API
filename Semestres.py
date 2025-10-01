class Semestre:

    def __init__(self, id_semestre, nombre, id_carrera):
        self.__id_semestre = id_semestre
        self.__nombre = nombre
        self.__id_carrera = id_carrera

    # Getters
    def get_id_semestre(self):
        return self.__id_semestre

    def get_nombre(self):
        return self.__nombre

    def get_id_carrera(self):
        return self.__id_carrera

    # Setters
    def set_id_semestre(self, id_semestre):
        self.__id_semestre = id_semestre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_id_carrera(self, id_carrera):
        self.__id_carrera = id_carrera


    def __str__(self):
        return f"Semestre {self.__id_semestre}, {self.__nombre}, {self.__id_carrera}"


