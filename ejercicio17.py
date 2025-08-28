empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

def empleados_con_alto_salario(diccionario, salario_minimo):
    return {id_emp: datos for id_emp, datos in diccionario.items() if datos[2] > salario_minimo}

print(empleados_con_alto_salario(empleados, 3000))
