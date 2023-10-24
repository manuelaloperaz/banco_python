usuarios = []

def registro_usuarios(id, nombre, apellido, cargo, area, salario):
    usuario = {
        'id': id,
        'nombre': nombre,
        'apellido': apellido,
        'cargo': cargo,
        'area': area,
        'salario': salario
    }
    usuarios.append(usuario)

def listar_empleados():
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']} {usuario['apellido']}, Cargo: {usuario['cargo']}, Área: {usuario['area']}, Salario: {usuario['salario']}")

def calcular_salario_neto(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            salario = usuario['salario']
            smlv = 1160000  
            if salario <= (2 * smlv):
                salario_neto = salario + 136454  
                return salario_neto
            else:
                salario_neto = salario
            return salario_neto
    

def imprimir_colilla(usuario):
    print(f"Colilla de Pago")
    print(f"Nombre: {usuario['nombre']} {usuario['apellido']}")
    print(f"Cargo: {usuario['cargo']}")
    print(f"Área: {usuario['area']}")
    print(f"Salario: {usuario['salario']}")
    print(f"Salario Neto: {calcular_salario_neto(id)}")

def visualizar_todos():
    for usuario in usuarios:
        imprimir_colilla(usuario)

def buscar_por_empleado(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            imprimir_colilla(usuario)

while True:
    print("Menú:")
    print("1. Registrarse")
    print("2. Listar Empleados")
    print("3. Calcular Salario Neto")
    print("4. Imprimir Colilla de Pago")
    print("5. Buscar por empleado")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id = input("Ingrese su ID: ")
        nombre = input("Nombre de usuario: ")
        apellido = input("Apellido: ")
        cargo = input("Cargo: ")
        area = input("Area: ")
        salario = int(input("Salario: "))  
        registro_usuarios(id, nombre, apellido, cargo, area, salario)
        print("Registro exitoso")

    elif opcion == "2":
        id = input("Ingrese su ID: ")
        for usuario in usuarios:
            if usuario['id'] == id and usuario['cargo'] == 'analista de recursos humanos':
                listar_empleados()
                break
        else:
            print("No tienes autorización para listar empleados.")

    elif opcion == "3":
        id = input("Ingrese el ID del empleado para calcular el salario neto: ")
        salario_neto = calcular_salario_neto(id)
        if salario_neto is not None:
            print(f"El salario neto es: {salario_neto}")
        else:
            print("Empleado no encontrado")

    elif opcion == "4":
        id = input("Ingrese su ID: ")
        for usuario in usuarios:
            if usuario['id'] == id:
                imprimir_colilla(usuario)

    elif opcion == "5":
        id = input("Ingrese el ID del empleado: ")
        buscar_por_empleado(id)

    elif opcion == "6":
        break
