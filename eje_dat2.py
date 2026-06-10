# Una tienda registra las columnas de 3 productos durante 4 semanas.
# Solicitar las columnas y almacenarlas en una matriz.
# Mostrar:
# Matriz completa
# Total vendido por producto

columnas = []

for producto in range(3):
    fila = []
    print("\nProducto ",producto + 1)
    for semana in range(4):
        dato = int(input(f"Semana {semana+1}: "))
        fila.append(dato)
    columnas.append(fila)

print("\nMatriz:")
for fila in columnas:
    print(fila)

print("\nTotales por producto")
for i in range(3):
    total =sum(columnas[i])
    print("Producto: ",i +1, " = ", total)