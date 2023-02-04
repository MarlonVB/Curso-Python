from model.Persona import Persona
class Profesor(Persona):
    def __int__(self, nombre, apellido, edad, genero, materia, titulo):
        Persona. __init__(self, nombre, apellido, edad, genero)
        self.materia = materia
        self.titulo = titulo