class Carrera():
    def __init__(self, id = 0, nombre = ""):
        self.__id = id
        self.__nombre = nombre

#Nombre
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

#ID
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

#KEYS
    def get_keys(self):
        return self.__id, self.__nombre


#STR
    def __str__(self):
        return f"Nombre Carrera: {self.__nombre}\n"
    