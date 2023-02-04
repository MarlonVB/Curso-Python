# Calculadora

# Variables para almacenar los números y la operación seleccionada
res = 0
num1 = ""
num2 = ""
operacion = ""

def input_numbers():
    """
    Función para pedir al usuario dos números.
    """
    global num1
    global num2
    num1 = input("Ingresa el primer número: ")
    num2 = input("Ingresa el segundo número: ")
    validate_numbers()

def input_operation():
    """
    Función para pedir al usuario la operación que desea realizar.
    """
    print("ENTRO")
    global operacion
    print("*** Operaciones ***\n1: Suma\n2: Resta\n3: Multiplicación\n4: División")
    operacion = input("Elige qué operación deseas realizar: ")
    execute_operation()

def input_again():
    """
    Función para pedir al usuario que ingrese de nuevo el segundo número.
    """
    global num2
    num2 = input("Ingresa de nuevo el segundo número: ")

def validate_numbers():
    """
    Función para validar si los valores ingresados son números.
    """
    global num1
    global num2
    if num1.isdigit() and num2.isdigit():
        input_operation()
    else:
        print("Uno de los valores ingresados no es un número.")
        input_numbers()

def execute_operation():
    # Realiza la operación seleccionada
    if operacion:
        if operacion == "1":
            res = int(num1) + int(num2)
            print(res)
        elif operacion == "2":
            res = int(num1) - int(num2)
            print(res)
        elif operacion == "3":
            res = int(num1) * int(num2)
            print(res)
        elif operacion == "4":
            if num2 != "0":
                res = int(num1) / int(num2)
                print(res)
            else:
                print("No se puede dividir un número por cero.")
                input_again()
        else:
            print("Operación no reconocida.")
            input_operation()
    else:
        print("No has elegido ninguna opción.")
        input_operation()

# Pide al usuario los números y la operación (PRIMERA LINEA EN EJECUTARSE)
input_numbers()