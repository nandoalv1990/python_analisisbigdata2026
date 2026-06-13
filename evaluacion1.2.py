# Programa donde se ingresan 5 subtotales, se hace una 
# sumatoria total, se calcula el iva
# se suma el iva con el total, y se imprimen total
# iva y total má iva
# Pero con FOR

print("Bienvenido...")

total = 0

for i in range(1, 6):
    subtotal = float(input(f"Ingresa subtotal {i}: "))
    total = total + subtotal

iva = total * 0.16
totalmasiva = total + iva

print("Total\t...",total)
print("IVA\t...",iva)
print("Total más IVA\t...",totalmasiva)