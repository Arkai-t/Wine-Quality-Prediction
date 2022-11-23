import pandas as pd

class WineCSVParser:
    def __init__(self, path) -> None:
        self.path = path

    def readCSV(self) -> pd.DataFrame:
        df =  pd.read_csv(self.path, header=0, index_col="Id")
        return df

    def writeNewWine(self, 
                    fixedAcidity : float, volatileAcidity : float, 
                    citricAcid : float, residualSugar : float, 
                    chlorides : float, freeSulfurDioxyde : float,
                    totalSulfurDioxyde : float, density : float,
                    pH : float, sulphates : float, 
                    alcohol : float, quality : int):
        
        # Get number of lines in the file to calculate the index of the line
        with open(self.path, 'r') as f:
            numLines = len(f.readlines())

        newEntry = pd.DataFrame([[fixedAcidity, volatileAcidity, citricAcid,
                                residualSugar, chlorides, freeSulfurDioxyde,
                                totalSulfurDioxyde, density, pH, sulphates,
                                alcohol, quality, (numLines -1)]])

        print(newEntry.to_string())

        newEntry.to_csv(self.path, header=0, index=False, mode='a')