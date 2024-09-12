# recommender.py

import pandas as pd
from sklearn.neighbors import NearestNeighbors

class Recommender:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.model = NearestNeighbors(n_neighbors=2, algorithm='auto')
        self.model.fit(self.data[['features']].tolist())

    def get_recommendations(self, product_id):
        index = self.data[self.data['id'] == product_id].index[0]
        distances, indices = self.model.kneighbors([self.data.iloc[index]['features']])
        recommendations = self.data.iloc[indices[0]]
        return recommendations
