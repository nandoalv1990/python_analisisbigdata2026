#Arbol genealógico
#Abuelo
#├── Padre
#│   ├── Hijo1
#│   └── Hijo2

class Nodo:
    #Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []
    
    def agregar_miembros(self, miembro):
        self.miembros.append(miembro)

    def mostrar(self, nivel = 0):
        print(" " * nivel + self.nombre)
        for miembro in self.miembros:
            miembro.mostrar(nivel + 4)

abuelo = Nodo("Gabo")
padre = Nodo("Padre")
hijo1 = Nodo("Yahir")
hijo2 = Nodo("Hijo2")

abuelo.agregar_miembros(padre)
padre.agregar_miembros(hijo1)
padre.agregar_miembros(hijo2)

abuelo.mostrar()


