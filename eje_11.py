# 
print("Bienvenido...")

d = int(input("Ingresa la cantidad de defectos encontrados: "))

if d <= 5:
    print("Lote aceptado")
elif d >= 6 and d <= 10:
    print("Lote en observacion")
else:
    print("Lote rechazado")

