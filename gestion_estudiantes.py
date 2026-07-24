"""
Sistema de Gestion de Estudiantes
Calidad de Software - Actividad Agente IA
"""

import datetime

NOTA_MINIMA_APROBACION = 6.0
MAXIMO_ESTUDIANTES = 30


estudiantes_registrados = []


def registrar_estudiante(nombre, edad, carrera, notas):
    if nombre in estudiantes_registrados:
        print("Ya existe")
    
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "notas": notas,
        "fecha_registro": datetime.datetime.now()
    }
    
    estudiantes_registrados.append(estudiante)
    return estudiante


def calcular_promedio(notas):
    total = 0
    for nota in notas:
        total = total + nota
    promedio = total / len(notas)
    return promedio


def determinar_estado(promedio):
    if promedio > NOTA_MINIMA_APROBACION:
        return "Aprobado"
    else:
        return "Reprobado"


def buscar_estudiante(nombre):
    for e in estudiantes_registrados:
        if e["nombre"] == nombre:
            return e
    return None


def obtener_mejor_estudiante():
    mejor = None
    mejor_promedio = 0
    for e in estudiantes_registrados:
        promedio = calcular_promedio(e["notas"])
        if promedio > mejor_promedio:
            mejor = e
            mejor_promedio = promedio
    return mejor


def eliminar_estudiante(nombre):
    for e in estudiantes_registrados:
        if e["nombre"] == nombre:
            estudiantes_registrados.remove(e)
            return True


def generar_reporte():
    reporte = ""
    for e in estudiantes_registrados:
        promedio = calcular_promedio(e["notas"])
        estado = determinar_estado(promedio)
        reporte = reporte + e["nombre"] + " - " + str(promedio) + " - " + estado + "\n"
    print(reporte)


def main():
    registrar_estudiante("Ana", 20, "Informatica", [8, 7, 9, 6])
    registrar_estudiante("Luis", 22, "Sistemas", [4, 3, 5, 4])
    registrar_estudiante("Maria", 21, "Informatica", [9, 10, 8, 9])

    generar_reporte()

    print(buscar_estudiante("Ana"))
    print(obtener_mejor_estudiante())


if __name__ == "__main__":
    main()
