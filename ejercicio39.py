def simular_mercado(precios_diarios, operaciones):
    beneficio = 0
    acciones = 0
    for tipo, dia in operaciones:
        if tipo == "compra":
            acciones += 1
            beneficio -= precios_diarios[dia]
        elif tipo == "venta":
            acciones -= 1
            beneficio += precios_diarios[dia]
    return beneficio

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]
print(simular_mercado(precios_diarios, operaciones))
