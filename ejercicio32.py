def simular_ventas(*ventas):
    total = 0
    for producto, cantidad, precio in ventas:
        total += cantidad * precio
    return total

print(simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0)))

