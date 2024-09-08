import pandas as pd
import os

# Crear carpeta data si no existe
carpeta_data = 'data'
os.makedirs(carpeta_data, exist_ok=True)

# Datos de ejemplo para ventas
datos_ventas = {
    'usuario_id': [1, 1, 2, 2, 3, 3],
    'producto_id': [101, 102, 101, 103, 102, 104],
    'calificacion': [5, 3, 4, 2, 4, 5]
}

# Datos de ejemplo para usuarios
datos_usuarios = {
    'usuario_id': [1, 2, 3],
    'nombre': ['Juan Pérez', 'Ana Gómez', 'Carlos Fernández']
}

# Crear DataFrames
df_ventas = pd.DataFrame(datos_ventas)
df_usuarios = pd.DataFrame(datos_usuarios)

# Guardar DataFrames como archivos CSV en la carpeta data
df_ventas.to_csv(os.path.join(carpeta_data, 'ventas.csv'), index=False)
df_usuarios.to_csv(os.path.join(carpeta_data, 'usuarios.csv'), index=False)

print("Archivos CSV creados con éxito en la carpeta 'data'.")
