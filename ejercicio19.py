resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def total_goles(diccionario):
    goles_a_favor = sum(valor[0] for valor in diccionario.values())
    goles_en_contra = sum(valor[1] for valor in diccionario.values())
    return goles_a_favor, goles_en_contra

print(total_goles(resultados))
