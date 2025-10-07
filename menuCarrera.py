import utils
from Carreras import Carrera
from DAOCarreras import DAOCarrera
import requests
from flask import jsonify

API_URL = "http://127.0.0.1:5000"

def menu(db):
    dao = DAOCarrera(db)
    opciones = {
        1: lambda: crear_carrera(),
        2: lambda: actualizar_carrera(),
        3: lambda: eliminar_carrera(),
        4: lambda: mostrar_carreras()
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

def crear_carrera():
    mostrar_carreras()
    nombre = input("Ingrese el nombre de la carrera: ")
    
    url = f"{API_URL}/carreras"
    r = requests.post(url, json={"nombre": nombre})
    
    if r.status_code == 200:
        print(f"Carrera creada: {nombre}")
    else:
        print("No se ha podido crear la carrera")

def actualizar_carrera():
    mostrar_carreras()
    id =  utils.validar_numero("Ingrese el ID de la carrera a actualizar: ")
    nombre = input("Ingrese el nuevo nombre de la carrera: ")

    url = f"{API_URL}/carreras"
    r = requests.put(url, json={"id": id, "nombre": nombre})

    if r.status_code == 200:
        print(f"Carrera actualizada: {nombre}")
    else:
        print("No se ha podido actualizar la carrera")

def eliminar_carrera():
    mostrar_carreras()
    id = utils.validar_numero("Ingrese el ID de la carrera a eliminar: ")

    url = f"{API_URL}/carreras"
    r = requests.delete(url, json={"id": id})

    if r.status_code == 200:
        print(f"Carrera eliminada")
    else:
        print("No se ha podido eliminar la carrera")

def mostrar_carreras():
    url = f"{API_URL}/carreras"
    r = requests.get(url)

    if r.status_code == 200:
        carreras = r.json()
        if carreras:
            print("\nCarreras registradas:")
            print("ID - Nombre")
            for carrera in carreras:
                print(f"{carrera['id']} - {carrera['nombre']}")
        else:
            print("No hay carreras registradas.")
    else:
        print("Error al consultar la API:", r.status_code)

