#importacion de librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Creacion de arreglos con numpy
# Arreglo de ventas por semana
ventas_semana= np.array([150,200,170,220,300,250,190])
print("Ventas por semana:", ventas_semana)
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

# Asegurar que las columnas sean numéricas
datos_ventas['Unidades Vendidas'] = pd.to_numeric(datos_ventas['Unidades Vendidas'], errors='coerce')
datos_ventas['Precio Unitario'] = pd.to_numeric(datos_ventas['Precio Unitario'], errors='coerce')

#Eliminar filas con datos faltantes
datos_ventas = datos_ventas.dropna(subset=['Producto', 'Unidades Vendidas', 'Precio Unitario'])

#Tabla de Datos de ventas 
print("\nDatos de ventas:\n", datos_ventas)
#Tabla de ventas totales (Unidades Vendidas * Precio Unitario)
datos_ventas['Ventas Totales'] = datos_ventas['Unidades Vendidas'] * datos_ventas['Precio Unitario']
print("\nDatos con Ventas Totales:\n", datos_ventas)


# Visualización de datos con matplotlib
# Lista de colores 
colores = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FFB266', '#B2FF66']

# Gráfico de pastel de Unidades Vendidas por Producto
plt.pie(datos_ventas['Unidades Vendidas'],
        labels=datos_ventas['Producto'].astype(str),
        autopct='%1.1f%%',
        startangle=90,
        colors=colores)

plt.title('Unidades Vendidas por Producto')
plt.axis('equal')
plt.show()