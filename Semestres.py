class Semestre:

    def __init__(self, id_semestre, nombre, id_carrera):
        self.__id_semestre = id_semestre
        self.__nombre = nombre
        self.__id_carrera = id_carrera

    # Getters
    def getIdSemestre(self):
        return self.__id_semestre

    def getNombre(self):
        return self.__nombre

    def getIdCarrera(self):
        return self.__id_carrera

    # Setters
    def setIdSemestre(self, id_semestre):
        self.__id_semestre = id_semestre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setIdCarrera(self, id_carrera):
        self.__id_carrera = id_carrera


    def __str__(self):
        return f"Semestre {self.__id_semestre}, {self.__nombre}, {self.__id_carrera}"



