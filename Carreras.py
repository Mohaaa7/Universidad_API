class Carrera():
    def __init__(self, nombre):
        self.__nombre = nombre

#Nombre
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
#STR
    def __str__(self):
        return f"Nombre Carrera: {self.__nombre}\n"
    