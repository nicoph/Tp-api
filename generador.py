import random
import json
import uuid



nombres = ["Juan", "Maria", "Carlos", "Lucia", "Jose", "Ana", "Martin", "Laura", "Diego", "Valentina",
           "Miguel", "Sofia", "Pedro", "Camila", "Fernando", "Abril", "Ricardo", "Agustina", "Gabriel", "Luz"]

apellidos = ["Gonzalez", "Rodriguez", "Fernandez", "Lopez", "Martinez", "Perez", "Gomez", "Sanchez", "Gimenez", "Torres"]

comisiones = [1, 2]

estudiantes = []

for _ in range(25):
    nombre = random.choice(nombres).encode('utf-8').decode('unicode-escape')
    apellido = random.choice(apellidos).encode('utf-8').decode('unicode-escape')
    comision = random.choice(comisiones)
    nota = random.randint(0, 100)
    legajo = f"{apellido[0]}-{random.randint(1, 9999):04d}-{comision}"
    estudiante = {
        "legajo": legajo,
        "nombre": nombre,
        "apellido": apellido,
        "comision": str(comision),
        "nota": str(nota),
        "id": str(uuid.uuid4())
    }
    estudiantes.append(estudiante)

# Guardar la lista de estudiantes en un archivo JSON
archivo_json = "estudiantes.json"

with open(archivo_json, 'w') as archivo:
    json.dump({"estudiantes": estudiantes}, archivo, indent=4, ensure_ascii=False)

print("Se generaron 25 estudiantes y se guardaron en el archivo estudiantes.json.")