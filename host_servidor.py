from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import uuid

app = Flask(__name__)
CORS(app)
archivo_json = "estudiantes.json"

@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    with open(archivo_json, 'r') as archivo:
        estudiantes = json.load(archivo)
    return jsonify(estudiantes)

@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    estudiante = request.get_json()
    estudiante['id'] = str(uuid.uuid4())  # Generar un ID único
    with open(archivo_json, 'r+') as archivo:
        data = json.load(archivo)
        data['estudiantes'].append(estudiante)
        archivo.seek(0)
        json.dump(data, archivo, indent=4)
    return jsonify(estudiante), 201


@app.route('/', methods=['GET'])
def ruta_raiz():
    with open("index.html", "r") as archivo:
        contenido_html = archivo.read()
    return contenido_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



