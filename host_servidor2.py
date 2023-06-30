from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import uuid
import statistics

app = Flask(__name__)
CORS(app)
archivo_json = "estudiantes.json"

@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    with open(archivo_json, 'r') as archivo:
        estudiantes = json.load(archivo)
    return jsonify(estudiantes)


@app.route('/estudiantes/legajo/<legajo>', methods=['GET'])
def buscar_estudiante_por_legajo(legajo):
    with open(archivo_json, 'r') as archivo:
        estudiantes = json.load(archivo)
    estudiante_encontrado = None
    for estudiante in estudiantes['estudiantes']:
        if estudiante['legajo'] == legajo:
            estudiante_encontrado = estudiante
            break
    if estudiante_encontrado:
        return jsonify(estudiante_encontrado)
    else:
        return jsonify({'mensaje': 'Estudiante no encontrado'}), 404

@app.route('/estudiantes/apellido/<string:apellido>', methods=['GET'])
def obtener_estudiantes_por_apellido(apellido):
    with open(archivo_json, 'r') as archivo:
        estudiantes = json.load(archivo)
    resultado = [estudiante for estudiante in estudiantes['estudiantes'] if estudiante['apellido'] == apellido]
    return jsonify(resultado)

@app.route('/notas', methods=['GET'])
def obtener_notas():
    with open(archivo_json, 'r') as archivo:
        estudiantes = json.load(archivo)
    notas = [int(estudiante['nota']) for estudiante in estudiantes['estudiantes']]
    resultado = {
        'mediana': statistics.median(notas),
        'media': statistics.mean(notas),
        'q1': statistics.quantiles(notas, n=4)[0],
        'q3': statistics.quantiles(notas, n=4)[-1]
    }
    return jsonify(resultado)

@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    estudiante = request.get_json()
    estudiante['id'] = str(uuid.uuid4())  # Generar un ID único
    estudiante['legajo'] = f"{estudiante['apellido'][0].upper()}-{str(len(estudiante['apellido'])).zfill(4)}-{uuid.uuid4().int % 10}"
    with open(archivo_json, 'r+') as archivo:
        data = json.load(archivo)
        data['estudiantes'].append(estudiante)
        archivo.seek(0)
        json.dump(data, archivo, indent=4)
    return jsonify(estudiante), 201

@app.route('/estudiantes/borrar/<string:legajo>', methods=['DELETE'])
def borrar_estudiante(legajo):
    with open(archivo_json, 'r+') as archivo:
        data = json.load(archivo)
        estudiantes = data['estudiantes']
        estudiantes = [estudiante for estudiante in estudiantes if estudiante['legajo'] != legajo]
        data['estudiantes'] = estudiantes
        archivo.seek(0)
        json.dump(data, archivo, indent=4)
        archivo.truncate()
    return jsonify({'message': 'Estudiante borrado exitosamente.'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)