# Values are based on database analysis and research

def isFixedAcidityValid(fixedAcidity : float) -> bool:
    return (fixedAcidity >= 1.0 and fixedAcidity <= 30.0)

def isVolatileAcidityValid(volatileAcidity : float) -> bool:
    return (volatileAcidity >= 0.0 and volatileAcidity <= 3.0)

def isCitricAcidValid(citricAcid : float) -> bool:
    return (citricAcid >= 0.0 and citricAcid <= 1.0)

def isResidualSugarValid(residualSugar : float) -> bool:
    return (residualSugar >= 0.0 and residualSugar <= 30.0)

def isChloridesValid(chlorides : float) -> bool:
    return (chlorides >= 0.0 and chlorides <= 1.0)

def isFreeSulfurDioxydeValid(freeSulfurDioxyde : float) -> bool:
    return (freeSulfurDioxyde >= 0.0 and freeSulfurDioxyde <= 200.0)

def isTotalSulfurDioxydeValid(totalSulfurDioxyde : float) -> bool:
    return (totalSulfurDioxyde >= 5.0 and totalSulfurDioxyde <= 300.0)

def isDensityValid(density : float) -> bool:
    return (density >= 0.95 and density <= 1.05)

def isPHValid(pH : float) -> bool:
    return (pH >= 2.0 and pH <= 5.0)

def isSulphatesValid(sulphates : float) -> bool:
    return (sulphates >= 0.0 and sulphates <= 3.0)

def isAlcoholValid(alcohol : float) -> bool:
    return (alcohol >= 0.0 and alcohol <= 15.0)

def isQualityValid(quality : int) -> bool:
    return (quality >= 0 and quality <= 10)

def isWineValid(fixedAcidity : float, volatileAcidity : float, 
                citricAcid : float, residualSugar : float, 
                chlorides : float, freeSulfurDioxyde : float,
                totalSulfurDioxyde : float, density : float,
                pH : float, sulphates : float, 
                alcohol : float) -> bool:

    return (isFixedAcidityValid(fixedAcidity)
            and isVolatileAcidityValid(volatileAcidity)
            and isCitricAcidValid(citricAcid)
            and isResidualSugarValid(residualSugar)
            and isChloridesValid(chlorides)
            and isFreeSulfurDioxydeValid(freeSulfurDioxyde)
            and isTotalSulfurDioxydeValid(totalSulfurDioxyde)
            and (freeSulfurDioxyde < totalSulfurDioxyde)
            and isDensityValid(density)
            and isPHValid(pH)
            and isSulphatesValid(sulphates)
            and isAlcoholValid(alcohol))                     


def isWineValidWithQuality(fixedAcidity : float, volatileAcidity : float, 
                citricAcid : float, residualSugar : float, 
                chlorides : float, freeSulfurDioxyde : float,
                totalSulfurDioxyde : float, density : float,
                pH : float, sulphates : float, 
                alcohol : float, quality : int) -> bool:

    return (isWineValid(fixedAcidity, volatileAcidity, citricAcid, residualSugar, 
                        chlorides, freeSulfurDioxyde, totalSulfurDioxyde, density, 
                        pH, sulphates, alcohol)
                       and isQualityValid(quality))
