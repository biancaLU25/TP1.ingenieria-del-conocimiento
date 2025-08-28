def analizar_tendencias(hashtags, tendencias, minimo=100):
    populares = []
    for tag, frecuencia in tendencias:
        if frecuencia > minimo and tag in hashtags:
            populares.append(tag)
    return populares

hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]
print(analizar_tendencias(hashtags, tendencias))

