import sklearn
print(sklearn.__version__)

# Importamos las librerías necesarias desde scikit-learn:
# - load_iris: para cargar el dataset de flores Iris.
# - train_test_split: para dividir los datos en entrenamiento y prueba.
# - LogisticRegression: algoritmo de regresión logística.
# - accuracy_score: para evaluar la precisión del modelo.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar el dataset Iris. Este dataset contiene datos de 150 flores,
# con 4 características (features) y una etiqueta (label) que representa
# la especie de la flor: Setosa, Versicolor o Virginica.

iris = load_iris()

# Asignamos las características (features) a la variable X
# y las etiquetas (labels) a la variable y.

X = iris.data   # variables predictoras (features)
y = iris.target # variable objetivo (label)

# Dividir los datos en conjunto de entrenamiento y prueba.
# 70% de los datos se usarán para entrenar el modelo, 30% paraprobarlo.
# random_state fija la semilla aleatoria para obtener resultados reproducibles.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
random_state=42)

# Crear un modelo de regresión logística.
# max_iter se establece en 200 para asegurar que el algoritmo converge.

model = LogisticRegression(max_iter=200)

# Entrenar el modelo con los datos de entrenamiento.
model.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba.
y_pred = model.predict(X_test)

# Evaluar el rendimiento del modelo calculando la precisión (accuracy),
# que indica el porcentaje de predicciones correctas sobre las totales.

print("Precision:", accuracy_score(y_test, y_pred))
