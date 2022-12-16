from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os
from dotenv import load_dotenv

from source.WineCSVParser import WineCSVParser
from source.WineModel import WineModel
from source import Stats
from source import WineValidation

load_dotenv()
MODEL_FILE = os.getenv('MODEL_FILE')
WINES_CSV = os.getenv('WINES_CSV')


wineModel = WineModel(MODEL_FILE, WINES_CSV)

app = FastAPI()

@app.post("/api/predict")
async def makePrediction(fixedAcidity : float, volatileAcidity : float, 
                         citricAcid : float, residualSugar : float, 
                         chlorides : float, freeSulfurDioxyde : float,
                         totalSulfurDioxyde : float, density : float,
                         pH : float, sulphates : float, 
                         alcohol : float) :

    if not WineValidation.isWineValid(fixedAcidity, volatileAcidity, citricAcid, residualSugar, 
                                      chlorides, freeSulfurDioxyde, totalSulfurDioxyde, density, 
                                      pH, sulphates, alcohol):
        raise HTTPException(status_code=422, detail="Wine not valid")

    wine = [fixedAcidity, volatileAcidity, citricAcid, residualSugar, chlorides, freeSulfurDioxyde, totalSulfurDioxyde, density, pH, sulphates, alcohol]

    res = wineModel.predict(wine)

    return {"wineScore": res}

@app.get("/api/predict")
async def getPerfectWine():
    return wineModel.bestWine()

@app.get("/api/model")
async def getSerializedModel():
    wineModel.save()

    return FileResponse(MODEL_FILE)

@app.get("/api/model/description")
async def getModelDescription():
    return Stats.readStats()

@app.put("/api/model")
async def addNewWine(fixedAcidity : float, volatileAcidity : float, 
                     citricAcid : float, residualSugar : float, 
                     chlorides : float, freeSulfurDioxyde : float,
                     totalSulfurDioxyde : float, density : float,
                     pH : float, sulphates : float, 
                     alcohol : float, quality : int):

    if not WineValidation.isWineValidWithQuality(fixedAcidity, volatileAcidity, citricAcid, residualSugar, 
                                      chlorides, freeSulfurDioxyde, totalSulfurDioxyde, density, 
                                      pH, sulphates, alcohol, quality):
        raise HTTPException(status_code=422, detail="Wine not valid")

    p = WineCSVParser(WINES_CSV)
    p.writeNewWine(fixedAcidity, volatileAcidity, citricAcid, residualSugar, 
                   chlorides, freeSulfurDioxyde, totalSulfurDioxyde, density, 
                   pH, sulphates, alcohol, quality)

    return {"message": "Wine added with success"}

@app.post("/api/model/retrain")
async def trainModel():
    wineModel.train()

    # TODO message erreur

    return {"message": "Model trained with success"}