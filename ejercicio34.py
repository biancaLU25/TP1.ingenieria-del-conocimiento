def analizar_encuestas(encuestas):
    resultados = {}
    for pregunta, respuestas in encuestas.items():
        frecuencias = {}
        for r in respuestas:
            frecuencias[r] = frecuencias.get(r, 0) + 1
        resultados[pregunta] = frecuencias
    return resultados

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}
print(analizar_encuestas(encuestas))