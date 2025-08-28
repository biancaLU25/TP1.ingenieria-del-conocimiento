ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def procesar_ventas(ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    return total, promedio

print(procesar_ventas(ventas_diarias))
