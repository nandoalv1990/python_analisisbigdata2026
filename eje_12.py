# Montoreo de inventario

print("Bienvenido al monitoreo de inventario")

inventario = 500

while inventario > 0:
    retiradas = int(input(f"Piezas disponibles {inventario}\nRetirar: "))
    while retiradas > inventario:
        print("Solicitud supera al inventario")
        retiradas = int(input(f"Piezas disponibles {inventario}\nRetirar: "))
    inventario = inventario - retiradas
    if inventario < 200:
        print("Inventario casi agotado")

print(f"No hay piezas disponibles\nGracias!")