#Primer programa Python

"""
El objeto "Persona" debe estar importado como un módulo en lugar de una clase.
Asegúrate de importar la clase "Persona" correctamente desde el módulo
donde se encuentra definida, y no el módulo entero en sí.

from model import Persona ----> MAL
from model.Persona import Persona ----> BIEN
"""
# CRUD de personas con POO y buenas prácticas de programación

from model.Persona import Persona

# Lista de objetos de tipo Persona
listPersons = []


# Se sugiere utilizar un switch-case en lugar de una serie de if-elif statements para una mejor legibilidad del código
def menu():
    """
    Muestra el menú principal y permite al usuario elegir una opción.
    """
    print("**** R E G I S T R O   D E   P E R S O N A S****")
    print("#### M E N U  P R I N C I P A L ####")
    print("1: Registrar persona")
    print("2: Editar persona")
    print("3: Listrar personas")
    print("4: Buscar persona")
    print("5: Eliminar persona")
    print("6: Eliminar todo")
    print("7: Salir")

    option = int(input("Elije una opción: "))

    # Se utiliza un switch-case para manejar la opción elegida por el usuario
    # En lugar de if-elif statements
    def option_case(option):
        if option == 1:
            return input_data()
        elif option == 2:
            return edit_person()
        elif option == 3:
            return print_list_persons()
        elif option == 4:
            return find_person()
        elif option == 5:
            return delete_person()
        elif option == 6:
            return delete_all()
        elif option == 7:
            return exit(0)

    switch_case = {
        1: input_data,
        2: edit_person,
        3: print_list_persons,
        4: find_person,
        5: delete_person,
        6: delete_all,
        7: exit
    }

    # Se llama a la función correspondiente según la opción elegida
    try:
        switch_case[option]()
    except KeyError:
        print("Opción inválida, por favor seleccione una opción válida.")

    # Se llama a la función recursivamente para seguir mostrando el menú
    # hasta que el usuario seleccione la opción 7 (salir)
    menu()

def input_data():
    """
    Método que recoge los datos de una persona y la registra en la lista
    """
    nombre = input("Ingrese el nombre de la persona: ")
    apellido = input("Ingrese el apellido de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    genero = input("Ingrese el género de la persona: ")

    register_person(nombre, apellido, edad, genero)

def register_person(nombre, apellido, edad, genero):
    """
    Método que registra una persona en la lista
    """
    persona = Persona(nombre, apellido, edad, genero)
    listPersons.append(persona)

def print_list_persons():
    """
    Método que muestra la lista de personas registradas
    """
    if listPersons:
        for person in listPersons:
            print(f"Nombre: {person.nombre} Apellido: {person.apellido} Edad: {person.edad} Género: {person.genero}")
    else:
        print("No hay personas registradas")

def find_person():
    """
    Método que busca una persona por su nombre
    """
    name_person_find = input("Ingrese en nombre de la persona que desea encontrar: ")
    exist = False
    for person in listPersons:
        if person.nombre == name_person_find:
            print(f"Nombre: {person.nombre} Apellido: {person.apellido} Edad: {person.edad} Género: {person.genero}")
            exist = True
            break
    if not exist:
        print("No se encontró una coincidencia")

def edit_person():
    """
    Modifica el nombre de una persona en la lista `listPersons`.
    """
    name_person = input("Ingrese el nombre de la persona a modificar: ")
    for person in listPersons:
        if person.nombre == name_person:
            person.nombre = input("Ingrese el nuevo nombre: ")
            break

def delete_person():
    """
    Elimina una persona de la lista `listPersons` por su nombre.
    """
    name_person = input("Ingrese el nombre de la persona a eliminar: ")
    exist = False
    for person in listPersons:
        if person.nombre in name_person:
            listPersons.remove(person)
            print("Persona eliminada satisfactoriamente")
            exist = True
            break
    if exist is False:
        print("No se encontro una coincidencia")

def delete_all():
    """
    Elimina todas las personas de la lista `listPersons`.
    """
    listPersons.clear()
    print("Todos los datos fueron eliminados")

menu()