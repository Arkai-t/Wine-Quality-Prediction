import pandas as pd

from source.WineCSVParser import WineCSVParser

TEST_CSV_FILE="./tests/test_wine.csv"

class TestWineCSVParser:
    def test_writeNewWine(self):
        parser = WineCSVParser(TEST_CSV_FILE)
        parser.writeNewWine(0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 2.2, 0.50, 0.55, 2)

        #Get last line without id
        lastLine = pd.read_csv(TEST_CSV_FILE).iloc[-1].to_list()[:-1]
        assert(lastLine == [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 2.2, 0.50, 0.55, 2])
        