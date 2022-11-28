import json

# mettre dans un fchier de conf
statsfile = "./data/stats"

def readStats() -> dict:
    with open(statsfile, "r") as file:
        dic = json.load(file)
        return dic

def saveStats(dic):
    with open(statsfile, "w") as file:
        r = json.dumps(dic, indent=4)
        file.write(r)