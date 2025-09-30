import mysql.connector 
from Carrera import Carrera

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

def crear_db(host, user, pwd, db):
    mydb = mysql.connector.connect(
        host= host,
        user= user,
        password= pwd,
        database= db
    )

    return mydb

def salir(db, cursor):
    print("Que pase una buena tarde.")
    cursor.close()
    db.close()
    exit()

def menu():
    db = crear_db("localhost", "root", "123456", "moha_haroon")
    cursor = db.cursor()
    carrera = Carrera(db, cursor)
    opciones = {
        1: carrera.menu,
        0: lambda: salir(db, cursor)
    }
    while True:
        opcion = validar_numero(
            "Seleccione una Opcion:\n"\
            "   1.- Gestionar Carreras.\n"\
            "   0.- Salir.\n",
            0,len(opciones)-1)
        accion = opciones.get(opcion)
        accion()


menu()