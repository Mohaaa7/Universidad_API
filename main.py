import mysql.connector 
import Carrera

#Ajustar
"""
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="universidad"
)
"""

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

def salir():
    print("Que pase una buena tarde.")
    exit()

def menu():
    opciones = {
        1: Carrera.menu_carrera,
        0: salir
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
print("Salí")