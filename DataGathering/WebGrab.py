import os.path
import pandas as pd
import requests

class Gather:
    def searchInit(self, pokemon, force):
        self.pokemon = pokemon.lower()
        self.force = force
        self.filePath = ".\\data\\"

        self.url = 'https://pokemondb.net/pokedex/' + self.pokemon
        self.csvFile = self.filePath + self.pokemon + ".csv"

        self.dataCheck()

    def webGet(self):
        rawHTML = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        testtable = pd.read_html(rawHTML.text)
        #print(testtable[3])
        rawTable = testtable[3]
        #testtable[3].to_csv(self.csvFile, index=None)
        if len(rawTable.columns) == 7:
            finalTable = rawTable.drop(rawTable.columns[[2, 5, 6]], axis = 1)
        if len(rawTable.columns) == 6:
            finalTable = rawTable.drop(rawTable.columns[[2, 5]], axis = 1)
        if len(rawTable.columns) <= 5:
            finalTable = rawTable.drop(rawTable.columns[2], axis = 1)
        
        print(finalTable)
        finalTable.to_csv(self.csvFile, index = None)
    
    def localGet(self):
        pass

    def dataCheck(self):
        if os.path.exists(self.csvFile) and not self.force:
            print("Data already exists in the database for this Pokemon.")
        elif os.path.exists(self.csvFile) and self.force:
            print("Updating tables from web!")
            self.webGet()
        else:
            print(self.filePath + self.pokemon + ".csv File Not Found!")
            self.webGet()