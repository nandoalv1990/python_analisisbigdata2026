# Programa de control de piezas en inventario

inventario = 1000
#El bucle se cumple hasta que el inventario esté en ceros
while inventario > 0:
    #Este valor se irá restando al inventario en cada vuelta hasta que sea cero
    salida = int(input("Piezas a retirar: "))
    #Este bucle no permite que las piezas ingresadas superen las piezas en el inventario
    while salida > inventario:
        print("ESO SUPERA LA CAPACIDAD!!\n")
        #Se vuelve a pedir el valor de salida
        salida = int(input("\tPiezas a retirar: "))
    #En cada vuelta se resta a el valor actual del inventario el valor ingresado por el usuario
    inventario = inventario - salida
    #Se imprime en nuevo valor
    print("Inventario restante: ", inventario, " pzs")
    #Si el valor es menor a 200 y mayor a cero, se encuentra en estado critico
    if inventario < 200 and inventario > 0:
        print("\tALERTA!\nINVENTARIO CRITICO!!")
#Finalmente si el inventario llega a cero, se termina el programa.
print("Inventario agotado")