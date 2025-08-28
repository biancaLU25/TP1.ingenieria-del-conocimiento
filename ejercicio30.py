def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    for usuario in usuarios:
        perfiles[usuario] = list(kwargs.items())  # convierto las config en lista
    return perfiles

usuarios = ["Ana", "Luis", "María"]
print(configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False))
