import tkinter as tk
import os.path
import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
import pprint


class Gather:
    def webGet(self):
        '''
        print("retrieving data from web")
        url = 'https://pokemondb.net/pokedex/' + self.pokemon.lower()
        rawHTML = requests.get(url)
        parsedPage = BeautifulSoup(rawHTML.text, 'html.parser')
        testFile = open('test.json', 'w')
        statTable = parsedPage.find_all("table", {"class":"vitals-table"})[3]
        print(statTable)
        statTableRows = statTable.find_all('tr')
        print(statTableRows)
        jsonRows = []
        for row in statTableRows:
            for cell in row.find_all(['th', "td"]):
                if cell.get_text() != '' and cell.get_text() != '\n\n':
                    jsonRows.append(cell.get_text())
        
        json.dump(jsonRows, testFile)
            

        testFile.close()
        '''
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

    def dataCheck(self, pokemon):
        self.pokemon = pokemon.lower()
        fileDirectory = ".\\data\\"

        print(self.pokemon)

        if os.path.exists(fileDirectory + pokemon.lower() + ".csv"):
            print("Data already exists in the database for this Pokemon.")
        else:
            print(fileDirectory + pokemon.lower() +".json File Not Found!")
            self.url = 'https://pokemondb.net/pokedex/' + self.pokemon
            self.csvFile = fileDirectory + str(self.pokemon) + ".csv"
            print(self.url, self.csvFile)
            self.webGet()