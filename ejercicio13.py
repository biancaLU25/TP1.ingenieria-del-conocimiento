estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

def promedio_estudiante(registro, matricula):
    calificaciones = registro[matricula]["calificaciones"].values()
    return sum(calificaciones) / len(calificaciones)


print(promedio_estudiante(estudiantes, estudiantes, 101))