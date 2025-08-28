def ranking_estudiantes(estudiantes):
    promedios = {}
    for id, materias in estudiantes.items():
        notas = []
        for califs in materias.values():
            notas.extend(califs)
        promedio = sum(notas) / len(notas)
        promedios[id] = promedio
    return sorted(promedios.items(), key=lambda x: x[1], reverse=True)

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}
print(ranking_estudiantes(estudiantes))