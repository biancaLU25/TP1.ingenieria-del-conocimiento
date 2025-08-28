def registro_empleado(nombre, edad, salario, **kwargs):
    datos = {"nombre": nombre, "edad": edad, "salario": salario}
    datos.update(kwargs)
    return datos

print(registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789"))
