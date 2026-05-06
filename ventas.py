import pandas as pd

#Leer el archivo con openpyxl (pip install pandas pip install openpyxl)

df = pd.read_excel("ventas.xlsx")

#Calcular total por producto
df["Total"] = df["Precio"] * df["Cantidad"]

#Mostrar resultados
print(df)

#Total general
print("Total general:",df["Total"].sum())