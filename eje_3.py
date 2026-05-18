#Programa que calcula el peso total que llevará un camión

print ("Bienvenido... \nCalculadora de peso")

cajas = int(input("Ingrese el numero de cajas: "))

pesoCaja = float(input("Ingrese peso por caja (kg): "))

totalpeso = cajas * pesoCaja

print("El peso final es ", totalpeso , "Kg")