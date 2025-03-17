class Persona:
    def __init__(self, nombre, apellido1, apellido2, edad):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.edad = edad
        
    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}, edad: {self.edad}"