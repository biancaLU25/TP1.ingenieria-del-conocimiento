paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

def calcular_costos(paquetes):
    return {destino: precio * dias for destino, precio, dias in paquetes}

print(calcular_costos(paquetes))
