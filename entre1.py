import pandas as pd
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#import des données 
X, y = load_boston(return_X_y=True)

#Séparation des données en jeu d'apprentissage et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 400)

#Scaling des données
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

#Sélection de variables
selector = SelectKBest(f_regression).fit(X_train, y_train)
X_train = selector.transform(X_train)
X_test = selector.transform(X_test)

from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

#Recherche des meilleurs paramètres pour chacun des modèles
estimators = [Lasso(),DecisionTreeRegressor(),RandomForestRegressor()]

best_params = {}
best_score = []
params = {'lasso':{'alpha':[0.01, 0.05, 0.1, 0.3, 0.8, 1]},
          'decision_tree':{'max_depth':[3,5,7,10],'max_features':[3,7]},
          'randomforest':{'n_estimators':[50,100,250],'max_depth':[3,5,7,10],'max_features':[3,7]}}

for i,j in zip(estimators,params.keys()):
    grid = GridSearchCV(i, param_grid = params[j], scoring = 'r2', cv = 3)
    grid.fit(X_train, y_train)
    best_params[j] = grid.best_params_
    best_score.append(grid.best_score_)

#Comparaison des modèles
lead_board = pd.DataFrame({'model':list(best_params.keys()),
                           'params':list(best_params.values()),
                           'score':best_score})

lead_board