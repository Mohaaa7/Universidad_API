from flask import Flask, jsonify, request as req
from DAOCarreras import DAOCarrera
from db import iniciar_sesion
from Carreras import Carrera

app = Flask(__name__)

db = iniciar_sesion()
dao = DAOCarrera(db)

# RUTAS DE CARRERAS
@app.route("/carreras", methods=["GET"])
def get_carreras():
    carreras = dao.get_carreras()
    
    result = []
    
    if carreras:
        for c in carreras:
            carrera_dict = {}
            carrera_dict["id"] = c.get_id()
            carrera_dict["nombre"] = c.get_nombre()

            result.append(carrera_dict)
        
        return jsonify(result)
    
    return jsonify({"error": "No se han encontrado carreras"})

@app.route("/carrera/<id>", methods=["GET"])
def get_carrera(id):
    carrera = Carrera(id)

    c = dao.get_carrera(carrera)
    
    if c:
        return jsonify({"id": c.get_id(), "nombre": c.get_nombre()})
    
    return jsonify({"error": "Carrera no encontrada"})

@app.route("/carreras", methods=["POST"])
def create_carrera():
    data = req.get_json()   
    nombre = data.get("nombre") 
    carrera = Carrera(0, nombre)
    
    c = dao.crear_carrera(carrera)
    
    if c:
        return jsonify({"mensaje": "Carrera creada"})
    else:
        return jsonify({"error": "No se pudo crear la carrera"})
    
@app.route("/carreras", methods=["PUT"])
def update_carrera():
    data = req.get_json()   
    id = data.get("id") 
    nombre = data.get("nombre") 

    carrera = Carrera(id, nombre)
    
    c = dao.actualizar_carrera(carrera)
    
    if c:
        return jsonify({"mensaje": "Carrera actualizada"})
    else:
        return jsonify({"error": "No se pudo actualizar la carrera"})

@app.route("/carreras", methods=["DELETE"])
def delete_carrera():
    data = req.get_json()   
    id = data.get("id") 

    carrera = Carrera(id)
    
    rowcount = dao.eliminar_carrera(carrera)
    
    if rowcount:
        return jsonify({"mensaje": "Carrera eliminada"})
    else:
        return jsonify({"error": "No se pudo eliminar la carrera"})


