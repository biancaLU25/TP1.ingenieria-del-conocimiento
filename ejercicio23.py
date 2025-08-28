inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def actualizar_inventario(stock, ventas):
    return [stock[i] - ventas[i] for i in range(len(stock))]

print(actualizar_inventario(inventario, ventas))
