temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def analisis_temperaturas(temp):
    media = sum(temp) / len(temp)
    maxima = max(temp)
    minima = min(temp)
    return media, maxima, minima

print(analisis_temperaturas(temperaturas))
