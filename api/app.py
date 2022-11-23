from fastapi import FastAPI

from source.WineCSVParser import WineCSVParser

app = FastAPI()

@app.post("/api/predict")
async def makePrediction(fixedAcidity : float, volatileAcidity : float, 
                         citricAcid : float, residualSugar : float, 
                         chlorides : float, freeSulfurDioxyde : float,
                         totalSulfurDioxyde : float, density : float,
                         pH : float, sulphates : float, 
                         alcohol : float, quality : int):
    return {"message": "I send a prediction for a given wine, between 0 and 10"}

@app.get("/api/predict")
async def getPerfectWine():
    return {"message": "I send a prediction for the perfect wine"}

@app.get("/api/model")
async def getSerializedModel():
    return {"message": "I send the model"}

@app.get("/api/model/description")
async def getModelDescription():
    return {"message": "I send parameters of the model, metrics on the last training, and other things"}

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
    return {"message": "I train the model with all data"}