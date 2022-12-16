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
        """

        Args:
            wine (list): list with all qualities of a wine

        Returns:
            _type_: _description_
        """
        res = self.model.predict([wine])
        return round(res[0])
    
    # Recherche dans db, pas forcément dans cette classe
    def bestWine(self) -> dict:
        """
        Return the characteristics of the best wine in the database

        Returns:
            dict: Characteristics of the best wine in the database
        """
        parser = WineCSVParser(self.trainDataPath)
        data = parser.readCSV()

        return data.iloc[self.stats["bestWineId"]]

    # retourner le Model
    def save(self):
        """
        Save the trained model in model.joblib file
        Update the statistics of the model
        """
        dump(self.model, self.path)
        Stats.saveStats(self.stats)

    # Load model
    def load(self):
        """
        Load the model from model.joblib if the file exist
        Else train the model
        """
        if os.path.isfile(self.path):
            self.model = load(self.path)
            self.stats = Stats.readStats()
        else:
            self.model = self.train()

    # Get model datas
    def getdatas(self) -> dict:
        """
        Return the statistics of the model

        Returns:
            dict: Statistics of the model
        """
        return self.stats
     
    # Train model + met à jour score
    def train(self):
        """
        Train the model and update the score

        Raises:
            Exception: If dataset doesn't exist
        """
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
