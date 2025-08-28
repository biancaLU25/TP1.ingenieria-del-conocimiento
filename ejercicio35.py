def optimizar_rutas(rutas, distancias_max):
    rutas_validas = []
    for i in range(len(rutas)):
        if rutas[i][2] <= distancias_max[i]:
            rutas_validas.append(rutas[i])
    return rutas_validas

rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]
print(optimizar_rutas(rutas, distancias_max))
