from flask import Flask, request, jsonify
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

app = Flask(__name__)

# Cargar datos
ventas_df = pd.read_csv('ventas.csv')
productos_df = pd.read_csv('productos.csv')

# Crear una matriz de usuario-producto
matriz_usuarios_productos = pd.pivot_table(ventas_df, index='usuario_id', columns='producto_id', values='monto', fill_value=0)

# Crear el modelo de recomendación
modelo = NearestNeighbors(n_neighbors=5, metric='cosine')
modelo.fit(matriz_usuarios_productos)

@app.route('/recomendaciones', methods=['GET'])
def obtener_recomendaciones():
    usuario_id = request.args.get('usuario_id', type=int)
    
    if usuario_id not in matriz_usuarios_productos.index:
        return jsonify({"error": f"El usuario_id {usuario_id} no existe en los datos."}), 400

    # Obtener el vector de usuario
    usuario_vector = matriz_usuarios_productos.loc[usuario_id].values.reshape(1, -1)
    
    # Encontrar vecinos más cercanos
    distancias, indices = modelo.kneighbors(usuario_vector)
    
    # Obtener los productos recomendados
    productos_recomendados = []
    for indice in indices[0]:
        producto_id = matriz_usuarios_productos.columns[indice]
        productos_recomendados.append(producto_id)
    
    # Crear una respuesta con los IDs de productos recomendados
    return jsonify({"productos_recomendados": productos_recomendados})

if __name__ == '__main__':
    app.run(debug=True)
