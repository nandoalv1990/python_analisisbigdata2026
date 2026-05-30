piezas = int(input("Ingresa las piezas producidas:"))

if piezas > 500:
    bono = 3000
else:
    if (piezas >= 300):
        bono = 1500
    else:
        bono = 0
print ("El bono es de $", bono)