productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]

def producto_mas_caro(lista):
    # max busca el mayor, key indica que compare por el precio (índice 1)
    return max(lista, key=lambda x: x[1])

print(producto_mas_caro(productos))
