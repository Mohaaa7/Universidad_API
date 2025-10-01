import mysql.connector 
from DAOCarreras import DAOCarrera
import utils


def crear_db(host, user, pwd, db):
    mydb = mysql.connector.connect(
        host= host,
        user= user,
        password= pwd,
        database= db
    )

    return mydb

def salir(db):
    print("Que pase una buena tarde.")
    db.close()
    exit()

def menu():
    user = input("Introduzca su nombre de usuario:")
    pwd = input("Introduzca su contraseña:")
    db = crear_db("localhost", user, pwd, "moha_haroon")
    carrera = DAOCarrera(db)
    opciones = {
        1: carrera.menu,
        0: lambda: salir(db)
    }
    while True:
        opcion = utils.validar_numero(
            "Seleccione una Opcion:\n"\
            "   1.- Gestionar Carreras.\n"\
            "   0.- Salir.\n",
            0,len(opciones)-1)
        accion = opciones.get(opcion)
        accion()


menu()