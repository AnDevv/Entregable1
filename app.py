from flask import Flask, jsonify, request
import pandas as pd
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

# Cargar datos
productos_df = pd.read_csv('data/productos.csv')
usuarios_df = pd.read_csv('data/usuarios.csv')

# Preparar el modelo de recomendación
# Aquí se usa un modelo simplificado; en producción, deberías ajustar esto
def recomendar_productos(usuario_id):
    # Simulación de un modelo de recomendación basado en vecinos más cercanos
    # Puedes mejorar esto según la lógica de tu sistema
    productos = productos_df[['id', 'nombre', 'descripcion', 'precio']].to_dict(orient='records')
    
    # Aquí se devolverán productos de ejemplo
    return productos[:5]  # Devuelve los primeros 5 productos para simplicidad

@app.route('/recomendaciones', methods=['GET'])
def obtener_recomendaciones():
    usuario_id = request.args.get('usuario_id', type=int)
    if usuario_id is None:
        return jsonify({'error': 'Falta el ID del usuario'}), 400

    productos_recomendados = recomendar_productos(usuario_id)
    return jsonify({'productos_recomendados': productos_recomendados})

if __name__ == '__main__':
    app.run(debug=True)
