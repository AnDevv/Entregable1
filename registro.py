import pandas as pd
import numpy as np

# Cargar datos desde un archivo CSV
ventas_df = pd.read_csv('ventas.csv')
usuarios_df = pd.read_csv('usuarios.csv')

# Mostrar las primeras filas de los datos
print(ventas_df.head())
print(usuarios_df.head())
