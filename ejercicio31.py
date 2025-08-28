def publicar(usuario, texto, **kwargs):
    publicacion = {
        "usuario": usuario,
        "texto": texto,
    }
    for clave, valor in kwargs.items():
        publicacion[clave] = valor
    return publicacion

print(publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100))
