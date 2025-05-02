#importacion de librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Creacion de arreglos con numpy
# Arreglo de valores de productividad semanal
productividad_semanal= np.array([75, 80, 90, 85, 70])
print("Ventas por semana:", productividad_semanal)

# Operaciones con arreglos
print("Promedio de productividad:",
np.mean(productividad_semanal))
print("Productividad máxima:",
np.max(productividad_semanal))
print("Productividad mínima:",
np.min(productividad_semanal))

# Lectura de archivos CSV con pandas
datos_empleados = pd.read_csv(r"C:\tec\octavo\plyf\Tema4\empleados.csv",
encoding='utf-8')

#Muestra los nombres de los empleados del departamento Ventas.
# Filtrar los empleados del departamento de Ventas
ventas = datos_empleados[datos_empleados['Departamento'] == 'Ventas']
print("\nDatos de los empleados del departamento Ventas:\n"
, ventas)
#Columna llamada Bono que contenga el 10% del salario
datos_empleados["Bono"] = datos_empleados["Salario"] * 0.10
print("\nDatos de los empleados con un BONO DEL 10%:\n"
, datos_empleados)

# Elimina columnas que contienen al menos un valor faltante
datos_empleados = datos_empleados.drop(columns=['Unnamed: 4'])
# Visualización de datos con matplotlib

# Gráfica de barras grafica de barras con el salario de cada empleado
plt.bar(datos_empleados['Nombre'],
datos_empleados['Salario'],
color='skyblue')
plt.title('Salario de cada empleado')
plt.xlabel('Nombre del empleado')
plt.ylabel('Salario')
plt.grid(axis='y')
plt.xticks(rotation=90)
plt.show()