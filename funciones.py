

salario = float(input("Ingrese el salario"))

def pagosEps(salario):
    return salario * 0.04

def pagoPension(salario):
    return salario * 0.04

pension = pagoPension(salario)
eps = pagosEps(salario)

def pagoNomina(salario, eps, pension):

    salario_neto = salario-eps-pension
    print(salario_neto)

pagoNomina(salario, eps, pension)

def pagoNomina2 (salario):
    eps = pagosEps(salario)
    pension = pagoPension(salario)
    salario_neto = salario - eps - pension
    print(salario_neto)

def ejemploCallback(valor):
    print (f"El salario neto es: {valor}")

def pagoNomina3(salario, ejemploCallback):
    eps = lambda salary: salario * 0.04
    pension = lambda salary: salario * 0.04
    salario_neto = salario - eps(salario) - pension(salario)
    ejemploCallback(salario_neto)
   # return salario_neto

pagoNomina2(salario)
pagoNomina3(salario,  ejemploCallback)

#bancolombia requiere calcular los salarios de su nueva start up pagui
#registrar id, nombre, apellido, cargo, area, salario
#requiere listar a los empleados
#requiere calcular el salario neto de cada uno, teniendo presente que si gana 2 SMLV se le paga auxilio de transporte
#imprimir colilla de pago
# un empleado podrá ingresar al sistema y buscar su colilla e imprimirla
# un analista de recursos humanos podra visualizar todos los empleados y todas las colillas, ademas buscar por empleado

usuarios= {}

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



while True:
    print("Menú:")
    print("1. Registrarse")
    print("2. Ingresar")
    print("3. xxx")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id = input("Ingrese su ID: ")
        nombre = input("Nombre de usuario: ")
        apellido = input("Apellido: ")
        cargo = input("Cargo: ")
        area = input("Area: ")
        salario = input("Salario: ")
        registro_usuarios(id, nombre, apellido, cargo, area, salario)
        print("Registro exitoso")

    elif opcion == "2":
        idlogin = input("Ingrese su ID: ")
        nombrelogin = input("Nombre de usuario: ")
        apellidologin = input("Apellido: ")
        cargologin = input("Cargo: ")




