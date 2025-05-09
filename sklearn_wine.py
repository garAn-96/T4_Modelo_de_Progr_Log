# Paso 1: Importar librerías necesarias
from sklearn.datasets import load_wine # Dataset de vinos
from sklearn.model_selection import train_test_split # Para dividir los datos
from sklearn.linear_model import LogisticRegression # Modelo declasificación
from sklearn.metrics import accuracy_score # Métrica de evaluación

# Paso 2: Cargar el dataset
wine = load_wine()

# Paso 3: Definir variables predictoras (X) y objetivo (y)
X = wine.data # Variables independientes: características químicas del vino
y = wine.target # Variable dependiente: tipo de vino (3 clases: 0, 1, 2)

# Paso 4: Dividir el dataset en conjunto de entrenamiento y prueba (70%-30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)

# Paso 5: Crear el modelo de regresión logística
model = LogisticRegression(max_iter=1000) # Se aumenta max_iter para asegurar convergencia

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Paso 6: Hacer predicciones con los datos de prueba
y_pred = model.predict(X_test)

# Paso 7: Evaluar la precisión del modelo
precision = accuracy_score(y_test, y_pred)

# Mostrar resultado
print("Precisión del modelo:", precision)