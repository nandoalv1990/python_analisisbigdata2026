# Programa donde se ingresan 5 subtotales, se hace una 
# sumatoria total, se calcula el iva
# se suma el iva con el total, y se imprimen total
# iva y total má iva

print(" Bienvenido...")
i = 1
sub1 = float(input(f"Ingresa el sub total {i}..."))
i = i + 1
sub2 = float(input(f"Ingresa el sub total {i}..."))
i = i + 1
sub3 = float(input(f"Ingresa el sub total {i}..."))
i = i + 1
sub4 = float(input(f"Ingresa el sub total {i}..."))
i = i + 1
sub5 = float(input(f"Ingresa el sub total {i}..."))

total = sub1 + sub2 + sub3 + sub4 + sub5
iva = total * 0.16
totalmasiva = total + iva

print("Total...",total )
print("IVA...",iva)
print("Total más IVA...",totalmasiva)