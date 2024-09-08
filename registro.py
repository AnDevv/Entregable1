import pandas as pd
import os

# Crear la carpeta 'data' si no existe
carpeta_data = 'data'
os.makedirs(carpeta_data, exist_ok=True)

# Datos para productos
datos_productos = {
    'producto_id': [101, 102, 103, 104],
    'nombre': ['Equipo de juego', 'Computadora Pc GAMER RYZEN', 'Silla ergonómica', 'Teclado mecánico'],
    'precio': [1200.99, 1250.49, 350.99, 89.99]
}

# Datos para usuarios
datos_usuarios = {
    'usuario_id': [1, 2, 3],
    'nombre': ['Juan Pérez', 'Ana Gómez', 'Carlos Fernández']
}

# Datos para ventas
datos_ventas = {
    'usuario_id': [1, 1, 2, 2, 3, 3],
    'producto_id': [101, 102, 101, 103, 102, 104],
    'calificacion': [5, 3, 4, 2, 4, 5]
}

# Crear DataFrames
df_productos = pd.DataFrame(datos_productos)
df_usuarios = pd.DataFrame(datos_usuarios)
df_ventas = pd.DataFrame(datos_ventas)

# Guardar los DataFrames como archivos CSV en la carpeta 'data'
df_productos.to_csv(os.path.join(carpeta_data, 'productos.csv'), index=False)
df_usuarios.to_csv(os.path.join(carpeta_data, 'usuarios.csv'), index=False)
df_ventas.to_csv(os.path.join(carpeta_data, 'ventas.csv'), index=False)

print("Archivos CSV creados con éxito en la carpeta 'data'.")
