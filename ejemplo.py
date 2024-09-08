# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
# Hacer reproducible el ejemplo
np.random.seed(1)
# Crear DataFrame con datos sintéticos
df = pd.DataFrame({
    'points': np.random.randint(30, size=1000),
    'assists': np.random.randint(12, size=1000),
    'drafted': np.random.randint(2, size=1000)
})
# Ver el DataFrame
print(df.head())
# Definir las variables predictoras y la variable de respuesta
X = df[['points', 'assists']]
y = df['drafted']

# Dividir el conjunto de datos en entrenamiento (70%) y prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Instanciar el modelo de regresión logística
logistic_regression = LogisticRegression()
# Entrenar el modelo con los datos de entrenamiento
logistic_regression.fit(X_train, y_train)
# Hacer predicciones sobre los datos de prueba
y_pred = logistic_regression.predict(X_test)
# Imprimir el informe de clasificación
print(classification_report(y_test, y_pred))
