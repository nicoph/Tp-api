import requests

servidor_url = "http://localhost:5000"

def obtener_estudiantes():
    response = requests.get(f"{servidor_url}/estudiantes")
    if response.status_code == 200:
        return response.json()
    else:
        return []

def agregar_estudiante(estudiante):
    response = requests.post(f"{servidor_url}/estudiantes", json=estudiante)
    if response.status_code == 201:
        return response.json()
    else:
        return None

# Agregar funciones para actualizar y eliminar estudiantes

