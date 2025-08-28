puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

def ordenar_puntuaciones(lista):
    return sorted(lista, key=lambda x: x[1], reverse=True)

print(ordenar_puntuaciones(puntuaciones))