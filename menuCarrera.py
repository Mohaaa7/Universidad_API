import utils
from Carreras import Carrera
from DAOCarreras import DAOCarrera
def menu(db):
    opciones = {
        1: lambda: crear_carrera(db),
        2: lambda: actualizar_carrera(db),
        3: lambda: eliminar_carrera(db),
        4: lambda: mostrar_carreras(db)
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

def crear_carrera(db):
    mostrar_carreras(db)
    nombre = input("Ingrese el nombre de la carrera: ")
    carrera = Carrera(0,nombre)
    dao = DAOCarrera(db)
    rowcount = dao.crear_carrera(carrera)
    if rowcount == 0:
        print("No se ha podido crear")
    else:
        print(f"Carrera creada: {nombre}")

def actualizar_carrera(db):
    mostrar_carreras(db)
    id =  utils.validar_numero("Ingrese el ID de la carrera a actualizar: ")
    nombre = input("Ingrese el nuevo nombre de la carrera: ")
    carrera = Carrera(id, nombre)
    dao = DAOCarrera(db)
    rowcount = dao.actualizar_carrera(carrera)
    if rowcount == 0:
        print("No se ha podido actualizar")
    else:
        print(f"Carrera con ID {id} actualizada a: {nombre}")


def eliminar_carrera(db):
    mostrar_carreras(db)
    id = utils.validar_numero("Ingrese el ID de la carrera a eliminar: ")
    carrera = Carrera(id)
    dao = DAOCarrera(db)
    rowcount = dao.actualizar_carrera(carrera)
    if rowcount == 0:
        print("No se ha podido eliminar")
    else:
        print(f"Carrera con ID {id} eliminada.")

def mostrar_carreras(db):
    dao = DAOCarrera(db)
    carreras = dao.mostrar_carreras()
    if carreras:
        print("\nCarreras registradas:")
        print("   ID - Nombre")
        for id_carrera, nombre in carreras:
            print(f"   {id_carrera} - {nombre}")
    else:
        print("No hay carreras registradas.")
