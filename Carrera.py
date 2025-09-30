class Carrera: 
    def  __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

    
def validar_numero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and maximo is not None:
                if not (minimo <= valor <= maximo):
                    print("La opción marcada no esta dentro del rango de opciones disponibles")
                    continue
            return valor
        except ValueError:
            print("Error: introduzca un número válido.")

def crear_carrera():
    print("Logica de crear_carrera")
def actualizar_carrera():
    print("Logica de actualizar_carrera")
def eliminar_carrera():
    print("Logica de eliminar_carrera")
def mostrar_carreras():
    print("Logica de mostrar_carreras")

def menu_carrera():
    opciones = {
        1: crear_carrera,
        2: actualizar_carrera,
        3: eliminar_carrera,
        4: mostrar_carreras
    }
    while True:
        opcion = validar_numero(
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