import pandas as pd
from sklearn.neighbors import NearestNeighbors
from flask import Flask, jsonify

# Crear una aplicación Flask
app = Flask(__name__)

# Leer los archivos CSV
ventas = pd.read_csv('data/ventas.csv')
usuarios = pd.read_csv('data/usuarios.csv')
productos = pd.read_csv('data/productos.csv')

# Función para preparar los datos y entrenar el modelo
def preparar_modelo():
    # Crear una tabla dinámica usuario-producto
    matriz_usuario_producto = ventas.pivot_table(index='usuario_id', columns='producto_id', values='calificacion').fillna(0)

    # Entrenar el modelo K-Nearest Neighbors
    modelo = NearestNeighbors(metric='cosine', algorithm='brute')
    modelo.fit(matriz_usuario_producto)
    
    return modelo, matriz_usuario_producto

modelo, matriz_usuario_producto = preparar_modelo()

# Función para obtener recomendaciones para un usuario
def obtener_recomendaciones(usuario_id, n_recomendaciones=5):
    distancias, indices = modelo.kneighbors([matriz_usuario_producto.loc[usuario_id]], n_neighbors=n_recomendaciones + 1)
    indices = indices.flatten()[1:]  # Excluir el propio usuario

    recomendaciones = []
    for i in indices:
        id_producto = matriz_usuario_producto.columns[i]
        producto = productos[productos['producto_id'] == id_producto].iloc[0]
        recomendaciones.append({
            'nombre': producto['nombre'],
            'precio': producto['precio']
        })
    
    return recomendaciones

# Ruta API para obtener recomendaciones
@app.route('/recomendaciones/<int:usuario_id>', methods=['GET'])
def recomendaciones(usuario_id):
    recomendaciones = obtener_recomendaciones(usuario_id)
    return jsonify(recomendaciones)

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
