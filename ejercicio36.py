def actualizar_inventario(inventario, tienda, **kwargs):
    if tienda not in inventario:
        inventario[tienda] = {}
    for producto, cambio in kwargs.items():
        inventario[tienda][producto] = inventario[tienda].get(producto, 0) + cambio
    return inventario

inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}
print(actualizar_inventario(inventario, tienda="Tienda A", producto_1=10, producto_2=-5))
