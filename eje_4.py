#Programa para calcular el consumo electrico de una maquina
print("Hola, este preograma calcula el consumo en W/h")

horas = float(input("Horas de operación: "))

consumo = float(input("Consumo en vatios (W): "))

if consumo < 1:
    print("Error el consumo no puede ser 0")
else:    
    total = horas * consumo
    print("El consumo en ", horas, "h fue de ", total, " W/h")