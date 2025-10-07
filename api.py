from flask import Flask, jsonify, request as req
from DAOCarreras import DAOCarrera
from db import crear_db
from Carreras import Carrera

app = Flask(__name__)

db = crear_db()
dao = DAOCarrera(db)

# RUTAS DE CARRERAS
@app.route("/carreras", methods=["GET"])
def get_carreras():
    carreras = dao.mostrar_carreras()
    
    result = []

    for c in carreras:
        carrera_dict = {}
        carrera_dict["id"] = c[0]
        carrera_dict["nombre"] = c[1]

        result.append(carrera_dict)

    return jsonify(result)

@app.route("/carreras", methods=["POST"])
def create_carrera():
    data = req.get_json()   
    nombre = data.get("nombre") 
    carrera = Carrera(0, nombre)
    
    rowcount = dao.crear_carrera(carrera)
    
    if rowcount:
        return jsonify({"mensaje": "Carrera creada"}), 200
    else:
        return jsonify({"error": "No se pudo crear la carrera"}), 500
    
@app.route("/carreras", methods=["PUT"])
def update_carrera():
    data = req.get_json()   
    id = data.get("id") 
    nombre = data.get("nombre") 

    carrera = Carrera(id, nombre)
    
    rowcount = dao.actualizar_carrera(carrera)
    
    if rowcount:
        return jsonify({"mensaje": "Carrera actualizada"}), 200
    else:
        return jsonify({"error": "No se pudo actualizar la carrera"}), 500


# RUTAS DE SEMESTRES

