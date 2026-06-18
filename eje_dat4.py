# El reto
# Combinar:
# clases
# listas
# matrices
# árboles

class Alumno:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = [] 

# Metodo para agregar calificaciones

    def agregar_calificaciones(self, cal):
        self.calificaciones.append(cal)

# Metodo para calcular el promedio

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

# Datos -> 
   # Arreglos para llenar la cantidad de alumnos
alumnos = []
   # Llenar nombre y matricula individual
cantidad =  int(input("Cantidad de alumnos: "))
for i in range(cantidad):
    nombre = input(f"{i + 1}. Nombre: ")
    matricula = input("Matricula: ")
    alumno = Alumno(nombre, matricula)
   # Otro para llenar calificaciones
    for j in range(3):
      cal = float(input(f"Calificación {j + 1}:"))
      alumno.agregar_calificaciones(cal)

    alumnos.append(alumno)
# Resultados -> 
   # Imprimir un reporte con cada atributo de las listas
print("\nREPORTE: ")
for alumno in alumnos:
    print("Alumno: ", alumno.nombre)
    print("Matricula: ", alumno.matricula)
    print("Calificaciones: ", alumno.calificaciones)
    print("Promedio: ", alumno.promedio())
# Importante: 
   # Cada carrera es un nodo de arbol (sistemas e industrial)
   # Los alumnos se almacenan en listas dentro de cada carrera
   # Cada alumno tiene una lista de calificaciones
      # Promedio por alumno
      # Promedio por carrera
   
   # Falta arbol de carreras
   # Falta calcular promedio por carrera (necesitamos carreras)
   # Buscar al mejor alumno de la uni