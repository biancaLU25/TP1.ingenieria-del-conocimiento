def actualizar_suscripcion(suscripciones, usuario, suscripcion, **kwargs):
    if usuario not in suscripciones:
        suscripciones[usuario] = []
    suscripciones[usuario].append(suscripcion)
    for opcion, valor in kwargs.items():
        suscripciones[usuario].append((opcion, valor))
    return suscripciones

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}
print(actualizar_suscripcion(suscripciones, usuario="Luis", suscripcion="mensual", auto_renovacion=True))

