import utils
from Carreras import Carrera
from DAOCarreras import DAOCarrera

def menu(db):
    dao = DAOCarrera(db)
    opciones = {
        1: lambda: crear_carrera(dao),
        2: lambda: actualizar_carrera(dao),
        3: lambda: eliminar_carrera(dao),
        4: lambda: mostrar_carreras(dao)
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

def crear_carrera(dao):
    mostrar_carreras(dao)
    nombre = input("Ingrese el nombre de la carrera: ")
    carrera = Carrera(0,nombre)
    rowcount = dao.crear_carrera(carrera)
    print(f"Carrera creada: {nombre}" if rowcount else "No se ha podido crear la carrera")


def actualizar_carrera(dao):
    mostrar_carreras(dao)
    id =  utils.validar_numero("Ingrese el ID de la carrera a actualizar: ")
    nombre = input("Ingrese el nuevo nombre de la carrera: ")
    carrera = Carrera(id, nombre)
    rowcount = dao.actualizar_carrera(carrera)
    print(f"Carrera con ID {id} actualizada a: {nombre}" if rowcount else "No se ha podido actualizar la carrera")


def eliminar_carrera(dao):
    mostrar_carreras(dao)
    id = utils.validar_numero("Ingrese el ID de la carrera a eliminar: ")
    carrera = Carrera(id)
    rowcount = dao.eliminar_carrera(carrera)
    print(f"Carrera con ID {id} eliminada." if rowcount else "No se encontró ninguna carrera con ese ID")

def mostrar_carreras(dao):
    carreras = dao.mostrar_carreras()
    if carreras:
        print("\nCarreras registradas:")
        print("   ID - Nombre")
        for id_carrera, nombre in carreras:
            print(f"   {id_carrera} - {nombre}")
    else:
        print("No hay carreras registradas.")
