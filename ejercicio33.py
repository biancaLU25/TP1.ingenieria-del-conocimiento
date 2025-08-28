def hacer_reserva(reservas, fecha, huesped, habitacion, precio):
    if fecha not in reservas:
        reservas[fecha] = []
    for r in reservas[fecha]:
        if r[1] == habitacion:  # chequeo si la habitación ya está ocupada
            return "Habitación no disponible"
    reservas[fecha].append((huesped, habitacion, precio))
    return reservas

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}
print(hacer_reserva(reservas, "2024-08-15", "Pedro", 101, 200))
