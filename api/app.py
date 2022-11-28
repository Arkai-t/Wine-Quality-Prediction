from fastapi import FastAPI

from source.WineCSVParser import WineCSVParser
from source.WineModel import WineModel

wineModel = WineModel()

app = FastAPI()

@app.post("/api/predict")
async def makePrediction(fixedAcidity : float, volatileAcidity : float, 
                         citricAcid : float, residualSugar : float, 
                         chlorides : float, freeSulfurDioxyde : float,
                         totalSulfurDioxyde : float, density : float,
                         pH : float, sulphates : float, 
                         alcohol : float) :

    wine = [fixedAcidity, volatileAcidity, citricAcid, residualSugar, chlorides, freeSulfurDioxyde, totalSulfurDioxyde, density, pH, sulphates, alcohol]

    res = wineModel.predict(wine)

    return {"wineScore": res}

@app.get("/api/predict")
async def getPerfectWine():
    # TODO
    return {"message": "I send a prediction for the perfect wine"}

@app.get("/api/model")
async def getSerializedModel():
    wineModel.save()

    return {"message": "I send the model"}

@app.get("/api/model/description")
async def getModelDescription():

    # TODO score est nul si modèle load

    return wineModel.getdatas()

@app.put("/api/model")
async def addNewWine(fixedAcidity : float, volatileAcidity : float, 
                     citricAcid : float, residualSugar : float, 
                     chlorides : float, freeSulfurDioxyde : float,
                     totalSulfurDioxyde : float, density : float,
                     pH : float, sulphates : float, 
                     alcohol : float, quality : int):

    # TODO: Validate data here

    p = WineCSVParser('./data/Wines.csv')
    p.writeNewWine(fixedAcidity, volatileAcidity, citricAcid, residualSugar, 
                   chlorides, freeSulfurDioxyde, totalSulfurDioxyde, density, 
                   pH, sulphates, alcohol, quality)

    return {"message": "I add a new wine entry in the csv"}

@app.post("/api/model/train")
async def trainModel():
    wineModel.train()

    # TODO message erreur

    return {}