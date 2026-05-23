# Calcula el área de un almacén, dados largo y ancho
# ¿Qué pasa si miden lo mismo?

print("Bienvenido, este programa calcula el área de un almacén")
largo = float(input("Ingrese el largo: "))
ancho = float(input("Ingrese el ancho: "))
if largo <= 0 or ancho <= 0:
    print("Los valores son inválidos")
else:
    if largo == ancho:
        print("¡Es un cuadrado!")
    else:
        if largo > ancho:
            print("Atención: normalmente el ancho debe ser menor que el largo")
            print("Verifique si los datos se ingresaron correctamente")
        else:
            print("Es un rectángulo")
    print("El área mide", largo * ancho, "metros cuadrados")