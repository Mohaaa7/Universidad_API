import menuCarrera
import utils
import menuSemestre
from db import crear_db

def salir(db):
    print("Que pase una buena tarde.")
    db.close()
    exit()

def iniciar_sesion():
    while True:
        user = input("Introduzca su nombre de usuario: ")
        pwd = input("Introduzca su contraseña: ")
        db = crear_db("localhost", user, pwd, "moha_haroon")
        if db:
            return db
        else:
            print("Intente nuevamente.\n")
            opcion = input("¿Desea volver a intentar? (s/n): ").strip().lower()
            if opcion != "s":
                exit()

def menu():
    db = iniciar_sesion()

    opciones = {
        1: lambda: menuCarrera.menu(db),
        2: lambda: menuSemestre.menu_semestre(db),
        0: lambda: salir(db)
    }

    while True:
        opcion = utils.validar_numero(
            "Seleccione una Opcion:\n"\
            "   1.- Gestionar Carreras.\n"\
            "   2.- Gestionar Semestres.\n"
            "   0.- Salir.\n",
            0,len(opciones)-1)
        accion = opciones.get(opcion)
        accion()

if __name__ == "__main__":
    menu()