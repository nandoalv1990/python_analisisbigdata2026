class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    def llamado(self):
        return print(self.nombre, " hace ", self.sonido)

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Guau!")
    def buscar(self, cosa):
        return print(self.nombre, " busca ", cosa)

perro = Perro("Albondiga")

perro.llamado()