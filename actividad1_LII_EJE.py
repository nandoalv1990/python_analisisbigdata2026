# Actividad 1 : Cálculo de costo de producción
# Autor: ISTI Fernando Alvarez
print("Bienvenido, este programa calcula costo total de prod..")


piezas = int(input("Ingrese el numero de piezas: "))
costo = float(input("Ingrese costo por pieza $:"))

diezcosto = costo * 0.10

costot = piezas * costo

print("El costo total de producción es $", costot + diezcosto)
print("El 10% que se andio es ", diezcosto)
