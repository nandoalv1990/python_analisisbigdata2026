#Crear un programa que solicite 5 calificaciones y las almacene en una lista. Al final deberá mostrar:
#Todas las calificaciones
#La mayor
#La menor
#El promedio

calificaciones = []

for i in range(5):
    cal = float(input("Ingrese la calificación: "))
    calificaciones.append(cal)

print("\nCalificaciones: ")
for cal in calificaciones:
    print(cal)
    prom = cal + cal

print("\nMayor: ",max(calificaciones))
print("Menor: ", min(calificaciones))
print("Promedio: ", sum(calificaciones) / len(calificaciones))