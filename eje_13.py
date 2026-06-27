# Producción semanal de una máquina

print("Bienvenido al registro semanal")

total = 0

for dia in range(1,8):
    print (f"###Total antes###\n\t {total}")
    produccion = int(input(f"Produccion del dia: {dia}: "))
    total = total + produccion
    print (f"###Total después###\n\t {total}")

promedio = total / 7

print(f"Produccion total: {total}")
print(f"Promedio de producción: {promedio}")

