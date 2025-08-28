notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def promedios_estudiantes(lista):
    return {nombre: sum(notas)/len(notas) for nombre, notas in lista}

print(promedios_estudiantes(notas_estudiantes))
