from flask import Flask, jsonify, request as req
from DAOCarreras import DAOCarrera
from db import crear_db

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


# RUTAS DE SEMESTRES

