#importacion de librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Creacion de arreglos con numpy
# Arreglo de ventas por semana
ventas_semana= np.array([150,200,170,220,300,250,190])
print("Ventas por semana:", ventas_semana)
#Glosario agregar que es Numpy,pandas, matplotlib
# Operaciones con arreglos
print("Promedio de ventas:",
np.mean(ventas_semana))
print("Ventas máxima:",
np.max(ventas_semana))
print("Ventas mínima:",
np.min(ventas_semana))

# Lectura de archivos CSV con pandas
datos_ventas = pd.read_csv(r"C:\tec\octavo\plyf\Tema4\ventas.csv",
encoding='utf-8')
print("\nDatos de ventas:\n"
, datos_ventas)

# Visualización de datos con matplotlib
# Gráfica de barras de Unidades Vendidas por Producto
plt.bar(datos_ventas['Producto'].astype(str),
datos_ventas['Unidades Vendidas'],
color='skyblue')
plt.title('Unidades Vendidas por Producto')
plt.xlabel('Producto')
plt.ylabel('Unidades Vendidas')
plt.grid(axis='y')
plt.show()