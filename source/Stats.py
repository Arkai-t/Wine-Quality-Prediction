import os
from dotenv import load_dotenv
import json

load_dotenv()

# mettre dans un fchier de conf
statsfile = os.getenv('STATS_FILE')

def readStats() -> dict:
    """
    Return the statistics from the model stores in data/stats.json

    Returns:
        dict: The statistics from the model
    """
    with open(statsfile, "r") as file:
        dic = json.load(file)
        return dic

def saveStats(dic) -> None:
    """
    Save the statistics from the model into data/stats.json

    Args:
        dic (_type_): Statistics from the model
    """
    with open(statsfile, "w") as file:
        r = json.dumps(dic, indent=4)
        file.write(r)