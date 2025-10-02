import utils
from Semestres import Semestre
from DAOSemestres import DAOSemestre

# Método menú para manejar el semestre
def menu_semestre(db):

    dao = DAOSemestre(db)
    
    opciones = {
        1: lambda: crear_semestre(dao),
        2: lambda: actualizar_semestre(dao),
        3: lambda: eliminar_semestre(dao),
        4: lambda: mostrar_semestres(dao)
    }
    
    while True:
        opcion = utils.validar_numero(
            "Seleccione una Opcion:\n"
            "   1.- Crear Semestre.\n"
            "   2.- Actualizar Semestre.\n"
            "   3.- Eliminar Semestre.\n"
            "   4.- Mostrar Semestres Disponibles.\n"
            "   0.- Volver.\n",
            0,4
        )
        if opcion == 0: return
        accion = opciones.get(opcion)
        accion()

# Método para crear semestres
def crear_semestre(dao):
    mostrar_semestres(dao)
    
    nombre = input("Ingrese el nombre del semestre: ")
    id_carrera = utils.validar_numero("Ingrese el ID de la carrera: ")
    semestre = Semestre(0, nombre, id_carrera)
    rowcount = dao.crear_semestre(semestre)
    
    print(f"Semestre creado: {nombre}" if rowcount else "No se ha podido crear el semestre")

# Método para actualizar semestres
def actualizar_semestre(dao):
    mostrar_semestres(dao)

    id_semestre = utils.validar_numero("Ingrese el ID del semestre a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del semestre: ")
    nuevo_id_carrera = utils.validar_numero("Ingrese el nuevo ID de la carrera: ")
    semestre = Semestre(id_semestre, nuevo_nombre, nuevo_id_carrera)
    rowcount = dao.actualizar_semestre(semestre)

    print(f"Semestre con ID {id_semestre} actualizado." if rowcount else "No se ha podido actualizar el semestre")

# Método para eliminar semestres
def eliminar_semestre(dao):
    mostrar_semestres(dao)

    id_semestre = utils.validar_numero("Ingrese el ID del semestre a eliminar: ")
    semestre = Semestre(id_semestre, "", 0)
    rowcount = dao.eliminar_semestre(semestre)

    print(f"Semestre con ID {id_semestre} eliminado." if rowcount else "No se ha podido eliminar el semestre")

# Método para mostrar semestres
def mostrar_semestres(dao):
    semestres = dao.mostrar_semestres()

    if semestres:
        print("\nSemestres registrados:")
        print("   ID - Nombre - ID Carrera")
        for idSemestre, nombre, idCarrera in semestres:
            print(f"   {idSemestre} - {nombre} - {idCarrera}")
    else:
        print("No hay semestres registrados.")




