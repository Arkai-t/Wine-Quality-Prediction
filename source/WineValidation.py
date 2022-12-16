def isWineValid(fixedAcidity : float, volatileAcidity : float, 
                citricAcid : float, residualSugar : float, 
                chlorides : float, freeSulfurDioxyde : float,
                totalSulfurDioxyde : float, density : float,
                pH : float, sulphates : float, 
                alcohol : float) -> bool:
    """
    Return if a given wine is a valid wine

    Args:
        fixedAcidity (float): _description_
        volatileAcidity (float): _description_
        citricAcid (float): _description_
        residualSugar (float): _description_
        chlorides (float): _description_
        freeSulfurDioxyde (float): _description_
        totalSulfurDioxyde (float): _description_
        density (float): _description_
        pH (float): _description_
        sulphates (float): _description_
        alcohol (float): _description_

    Returns:
        bool: is the wine valid
    """

    # Values are based on database analysis and research
    return not ((fixedAcidity < 1.0 or fixedAcidity > 30.0) and (volatileAcidity < 0.0 or volatileAcidity > 3.0)             \
            and (citricAcid < 0.0 or citricAcid > 1.0) and (residualSugar < 0.0 or residualSugar > 30)                  \
            and (chlorides < 0.0 or chlorides > 1.0) and (freeSulfurDioxyde < 0.0 or freeSulfurDioxyde > 300.0)         \
            and (totalSulfurDioxyde < 5.0 or totalSulfurDioxyde > 300.0) and (freeSulfurDioxyde > totalSulfurDioxyde)   \
            and (density < 0.95 or density > 1.05) and (pH < 0.0 or pH > 14.0) and (sulphates < 0.0 or sulphates > 3.0) \
            and (alcohol < 0.0 or alcohol > 15.0))


def isWineValidWithQuality(fixedAcidity : float, volatileAcidity : float, 
                citricAcid : float, residualSugar : float, 
                chlorides : float, freeSulfurDioxyde : float,
                totalSulfurDioxyde : float, density : float,
                pH : float, sulphates : float, 
                alcohol : float, quality : int) -> bool:

    return (isWineValid(fixedAcidity, volatileAcidity, citricAcid, residualSugar, 
                        chlorides, freeSulfurDioxyde, totalSulfurDioxyde, density, 
                        pH, sulphates, alcohol)
                       and (quality >= 0 or quality <= 10))
