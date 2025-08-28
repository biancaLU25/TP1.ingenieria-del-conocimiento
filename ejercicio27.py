ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def estadisticas_ventas(ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    maximo = max(ventas)
    mes_max = ventas.index(maximo) + 1
    return {"total": total, "promedio": promedio, "mes_max": mes_max}

print(estadisticas_ventas(ventas_mensuales))
