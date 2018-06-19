import tkinter as tk
import os.path
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
        testFile = open('test.txt', 'w')
        statTable = parsedPage.find_all("table", {"class":"vitals-table"})[3]
        print(statTable)
        statTableHeaders = statTable. find_all('th')
        print(statTableHeaders)
        for header in statTableHeaders:
            statNames = []
            statNames.append(header.get_text())
        print(statNames)
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