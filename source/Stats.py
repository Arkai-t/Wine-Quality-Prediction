import os
from dotenv import load_dotenv
import json

load_dotenv()

# mettre dans un fchier de conf
statsfile = os.getenv('STATS_FILE')

def readStats() -> dict:
    with open(statsfile, "r") as file:
        dic = json.load(file)
        return dic

def saveStats(dic):
    with open(statsfile, "w") as file:
        r = json.dumps(dic, indent=4)
        file.write(r)