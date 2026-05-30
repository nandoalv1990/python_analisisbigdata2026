#Clase que define a una persona
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


# Crear objeto
persona1 = Persona("Fernando", 30)
persona2 = Persona("Juan", 20)

# Mostrar información
persona1.mostrar_datos()
persona2.mostrar_datos()