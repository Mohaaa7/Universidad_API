import mysql.connector 

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

