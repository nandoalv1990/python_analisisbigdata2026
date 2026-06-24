# Creación de un dataframe

import pandas as pd

nombres = []
calificaciones = []

for i in range(5):
    nombre = input("Nombre del alumno: ")
    calificacion = float(input("Calificacion: "))

    nombres.append(nombre)
    calificaciones.append(calificacion)

datos = {
    "Nombre" : nombres,
    "Calificacion" : calificaciones
}

df = pd.DataFrame(datos)

print("\n=== Tabla de calificaciones ===")
print(df)

print("\nPromedio: ", df["Calificacion"].mean())

print("Mayor: ", df["Calificacion"].max())

print("Menor: ", df["Calificacion"].min())