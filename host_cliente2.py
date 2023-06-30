import requests

servidor_url = ""

def obtener_ip_servidor():
    global servidor_url
    servidor_url = input("Ingrese la IP del servidor: ")
    print("Conexión establecida con el servidor:", servidor_url)

def obtener_estudiantes():
    response = requests.get(f"http://{servidor_url}:5000/estudiantes")
    if response.status_code == 200:
        estudiantes = response.json()
        if estudiantes:
            for estudiante in estudiantes["estudiantes"]:
                legajo = estudiante["legajo"]
                nombre = estudiante["nombre"]
                apellido = estudiante["apellido"]
                comision = estudiante["comision"]
                nota = estudiante["nota"]
                print(f"Legajo: {legajo}, Nombre: {nombre}, Apellido: {apellido}, Comisión: {comision}, Nota: {nota}")
        else:
            print("No se encontraron estudiantes.")
    else:
        print("Error al obtener los estudiantes.")

def consultar_estudiante_por_legajo():
    legajo = input("Ingrese el legajo del estudiante: ")
    response = requests.get(f"http://{servidor_url}:5000/estudiantes/legajo/{legajo}")
    if response.status_code == 200:
        estudiantes = response.json()
        if estudiantes:
                legajo = estudiantes["legajo"]
                nombre = estudiantes["nombre"]
                apellido = estudiantes["apellido"]
                comision = estudiantes["comision"]
                nota = estudiantes["nota"]
                print(f"Legajo: {legajo}, Nombre: {nombre}, Apellido: {apellido}, Comisión: {comision}, Nota: {nota}")
        else:
            print("No se encontraron estudiantes con ese legajo.")
    else:
        print("Error al obtener los estudiantes.")

def consultar_estudiante_por_apellido():
    apellido = input("Ingrese el apellido del estudiante: ")
    response = requests.get(f"http://{servidor_url}:5000/estudiantes/apellido/{apellido}")
    if response.status_code == 200:
        estudiantes = response.json()
        if estudiantes:
            for estudiante in estudiantes:
                legajo = estudiante["legajo"]
                nombre = estudiante["nombre"]
                apellido = estudiante["apellido"]
                comision = estudiante["comision"]
                nota = estudiante["nota"]
                print(f"Legajo: {legajo}, Nombre: {nombre}, Apellido: {apellido}, Comisión: {comision}, Nota: {nota}")
        else:
            print("No se encontraron estudiantes.")
    else:
        print("Error al obtener los estudiantes.")

def consultar_notas():
    response = requests.get(f"http://{servidor_url}:5000/notas")
    if response.status_code == 200:
        data = response.json()
        print("Estadísticas de notas:")
        print(f"Mediana: {data['mediana']}")
        print(f"Media: {data['media']}")
        print(f"Q1: {data['q1']}")
        print(f"Q3: {data['q3']}")
    else:
        print("Error al obtener los estudiantes y las estadísticas.")

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    comision = input("Ingrese la comisión del estudiante: ")
    nota = input("Ingrese la nota del estudiante: ")
    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "comision": comision,
        "nota": nota
    }
    response = requests.post(f"http://{servidor_url}:5000/estudiantes", json=estudiante)
    if response.status_code == 201:
        estudiante_creado = response.json()
        print("Estudiante agregado:", estudiante_creado)
    else:
        print("Error al agregar el estudiante.")

def borrar_estudiante():
    legajo = input("Ingrese el legajo del estudiante a borrar: ")
    response = requests.delete(f"http://{servidor_url}:5000/estudiantes/borrar/{legajo}")
    if response.status_code == 200:
        print("Estudiante borrado exitosamente.")
    else:
        print("Error al eliminar el estudiante")

def mostrar_menu():
    print("\n")
    print("----- Menú de Opciones -----")
    print("1. Recuperar lista de estudiantes")
    print("2. Consultar estudiante por legajo")
    print("3. Consultar estudiante por apellido")
    print("4. Consultar notas")
    print("5. Agregar estudiante")
    print("6. Borrar estudiante")
    print("0. Salir")
    print("-----------------------------")
    print("\n")

def main():
    obtener_ip_servidor()

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            estudiantes = obtener_estudiantes()
            if estudiantes:
                for estudiante in estudiantes:
                    print(estudiante)
            else:
                print("No se encontraron estudiantes.")

        elif opcion == "2":
            consultar_estudiante_por_legajo()

        elif opcion == "3":
            consultar_estudiante_por_apellido()

        elif opcion == "4":
            consultar_notas()

        elif opcion == "5":
            agregar_estudiante()

        elif opcion == "6":
            borrar_estudiante()

        elif opcion == "0":
            print("Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")
    
if __name__ == "__main__":
    main()