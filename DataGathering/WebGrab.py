import tkinter as tk
import os.path
import pandas
import json
import requests
from bs4 import BeautifulSoup
import pprint


class Gather:
    def webGet(self):
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

    def dataCheck(self, pokemon):
        self.pokemon = pokemon
        fileDirectory = ".\\data\\"

        print(self.pokemon)

        if os.path.exists(fileDirectory + pokemon.lower() + ".json"):
            print("True")
        else:
            print(fileDirectory + pokemon.lower() +".json File Not Found!")
            self.webGet()