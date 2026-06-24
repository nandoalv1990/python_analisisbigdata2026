# Producción semanal de una máquina

print("Bienvenido")

total = 0

for dia in range(1, 6):
    produccion = int(input(f"Produccion del dia: {dia}: "))
    total = total + produccion

