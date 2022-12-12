import pandas as pd

class WineCSVParser:
    def __init__(self, path) -> None:
        """

        Args:
            path (str): path used for a csv file with wine data
        """
        self.path = path

    def readCSV(self) -> pd.DataFrame:
        """
        Read a csv file with wines data

        Returns:
            pd.DataFrame: _description_
        """
        df =  pd.read_csv(self.path, header=0, index_col="Id")
        return df

    def writeNewWine(self, 
                    fixedAcidity : float, volatileAcidity : float, 
                    citricAcid : float, residualSugar : float, 
                    chlorides : float, freeSulfurDioxyde : float,
                    totalSulfurDioxyde : float, density : float,
                    pH : float, sulphates : float, 
                    alcohol : float, quality : int):
        """
        Add a new wine in the csv file

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
            quality (int): _description_
        """
        
        # Get last index
        with open(self.path, 'r') as f:
            lastLine = f.readlines()[-1]
            lastIndex = lastLine.split(',')[-1]

        newEntry = pd.DataFrame([[fixedAcidity, volatileAcidity, citricAcid,
                                residualSugar, chlorides, freeSulfurDioxyde,
                                totalSulfurDioxyde, density, pH, sulphates,
                                alcohol, quality, (int(lastIndex) +1)]])

        print(newEntry.to_string())

        newEntry.to_csv(self.path, header=0, index=False, mode='a')