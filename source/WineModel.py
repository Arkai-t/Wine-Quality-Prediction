import os
from sklearn.linear_model import LinearRegression
from joblib import dump, load

from WineCSVParser import WineCSVParser

class WineModel:
    model: LinearRegression
    score : float

    def __init__(self):
        self.load()
    
    def predict(self, wine):
        res = self.model.predict([wine])
        return round(res)
    
    # Recherche dans db, pas forcément dans cette classe
    def bestWine():
        pass

    # retourner le Model
    def save(self):
        dump(self.model, "./data/model.joblib")

    # Load model
    def load(self):
        if os.path.isfile("./data/model.joblib"):
            self.model = load("./data/model.joblib")
        else:
            self.model = self.train()

    # Get model datas
    def getdatas(self):
        return {"score": self.score, "coeffs": self.model.coef_}
     
    # Train model + met à jour score
    def train(self):
        if not os.path.isfile("./data/Wines.csv"):
            raise Exception("No dataset")
        
        parser = WineCSVParser("./data/Wines.csv")
        data = parser.readCSV()

        X = data[list(data.columns)[:-1]]
        Y = data['quality']
        self.model = LinearRegression().fit(X, Y)

        self.score = self.model.score(X,Y)
