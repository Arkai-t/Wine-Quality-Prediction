import os
from sklearn.linear_model import LinearRegression
from joblib import dump, load

from source.WineCSVParser import WineCSVParser
from source import Stats

class WineModel:
    model : LinearRegression
    stats : dict = 0

    def __init__(self, path, trainDataPath):
        self.path = path
        self.trainDataPath = trainDataPath
        self.load()
    
    def predict(self, wine):
        res = self.model.predict([wine])
        return round(res[0])
    
    # Recherche dans db, pas forcément dans cette classe
    def bestWine(self):
        return self.stats["bestWineId"]

    # retourner le Model
    def save(self):
        dump(self.model, self.path)
        Stats.saveStats(self.stats)

    # Load model
    def load(self):
        if os.path.isfile(self.path):
            self.model = load(self.path)
            self.stats = Stats.readStats()
        else:
            self.model = self.train()

    # Get model datas
    def getdatas(self):
        return self.stats
     
    # Train model + met à jour score
    def train(self):
        if not os.path.isfile(self.trainDataPath):
            raise Exception("No dataset")
        
        parser = WineCSVParser(self.trainDataPath)
        data = parser.readCSV()

        X = data[list(data.columns)[:-1]]
        Y = data['quality']
        self.model = LinearRegression().fit(X, Y)

        d = {}
        d["score"] = self.model.score(X, Y)
        d["coef"] = self.model.coef_.tolist()
        d["bestWineId"] = int(data['quality'].idxmax())

        self.stats = d
