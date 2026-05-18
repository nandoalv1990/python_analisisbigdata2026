#Ejercicio 6

print("Bienvenido, este programa define la calidad de una pieza")

def_piezas = int(input("Ingrese el numero de defectos en la pieza:"))

#if def_piezas == 0:
#    print("La pieza es perfecta")
#else:
#    print("La pieza es imperfecta")

if def_piezas == 0:
    print("La pieza es perfecta")
else: 
    if def_piezas <= 3:
        print("La pieza es reutilizable")
    else:
        print("La pieza es imperfecta")