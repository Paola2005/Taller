def empresas_con_mas_de_10_empleados_en_rrhh(empresas):
    count = 0
    for empresa, departamentos in empresas.items():
        for departamento in departamentos:
            if departamento["departamento"] == "Recursos Humanos" and departamento["empleados"] > 10:
                count += 1
                break
    print(f"Número de empresas con más de 10 empleados en Recursos Humanos: {count}")

def promedio_empleados_por_departamento(empresas):
    departamentos = {}
    for empresa, deptos in empresas.items():
        for depto in deptos:
            departamento = depto["departamento"]
            empleados = depto["empleados"]
            if departamento in departamentos:
                departamentos[departamento]["total_empleados"] += empleados
                departamentos[departamento]["total_empresas"] += 1
            else:
                departamentos[departamento] = {"total_empleados": empleados, "total_empresas": 1}

    print("Promedio de empleados por departamento:")
    for departamento, data in departamentos.items():
        promedio = data["total_empleados"] / data["total_empresas"]
        print(f"{departamento}: {promedio}")

def empresas_con_operaciones_doble_ventas(empresas):
    count = 0
    for empresa, departamentos in empresas.items():
        empleados_ventas = None
        empleados_operaciones = None
        for departamento in departamentos:
            if departamento["departamento"] == "Ventas":
                empleados_ventas = departamento["empleados"]
            elif departamento["departamento"] == "Operaciones":
                empleados_operaciones = departamento["empleados"]

        if empleados_ventas and empleados_operaciones and empleados_operaciones >= 2 * empleados_ventas:
            count += 1

    print(f"Número de empresas con el doble o más empleados en Operaciones que en Ventas: {count}")

def reorganizar_por_departamento(empresas):
    departamentos = {}
    for empresa, deptos in empresas.items():
        for depto in deptos:
            departamento = depto["departamento"]
            empleados = depto["empleados"]
            if departamento in departamentos:
                departamentos[departamento].append({empresa: empleados})
            else:
                departamentos[departamento] = [{empresa: empleados}]
    
    print("Estructura de datos reorganizada por departamento:")
    for departamento, data in departamentos.items():
        print(departamento, data)

empresas = {
    "Empresa 1": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 4}, {"departamento": "Ventas", "empleados": 10}, {"departamento": "Operaciones", "empleados": 25}],
    "Empresa 2": [{"departamento": "Recursos Humanos", "empleados": 10}, {"departamento": "Contabilidad", "empleados": 15}, {"departamento": "Ventas", "empleados": 25}, {"departamento": "Operaciones", "empleados": 41}],
    "Empresa 3": [{"departamento": "Recursos Humanos", "empleados": 8}, {"departamento": "Contabilidad", "empleados": 20}, {"departamento": "Ventas", "empleados": 32}, {"departamento": "Operaciones", "empleados": 56}],
    "Empresa 4": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 8}, {"departamento": "Ventas", "empleados": 15}, {"departamento": "Operaciones", "empleados": 29}],
    "Empresa 5": [{"departamento": "Recursos Humanos", "empleados": 20}, {"departamento": "Contabilidad", "empleados": 35}, {"departamento": "Ventas", "empleados": 58}, {"departamento": "Operaciones", "empleados": 97}],
}

while True:
    print("\n--- Menú ---")
    print("1. Mostrar cuántas empresas tienen más de 10 empleados en Recursos Humanos")
    print("2. Mostrar el promedio de empleados por departamento")
    print("3. Mostrar cuántas empresas tienen el doble o más empleados en Operaciones que en Ventas")
    print("4. Mostrar una nueva estructura de datos reorganizada por departamento")
    print("5. Salir")
    opcion = int(input("Ingrese una opción (1-5): "))

    if opcion == 1:
        empresas_con_mas_de_10_empleados_en_rrhh(empresas)
    elif opcion == 2:
        promedio_empleados_por_departamento(empresas)
    elif opcion == 3:
        empresas_con_operaciones_doble_ventas(empresas)
    elif opcion == 4:
        reorganizar_por_departamento(empresas)
    elif opcion == 5:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida (1-5).")