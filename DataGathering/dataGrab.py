import sys
from os import path
from bs4 import BeautifulSoup as soup
import pandas as pd
import requests
import data.pokeDatabase as sqldata

class Gather:
    def searchInit(self, pokemon, force):
        self.pokemon = pokemon.lower()
        self.force = force
        self.filePath = path.join(".", "data")

        self.url = 'https://pokemondb.net/pokedex/' + self.pokemon
        self.csvFile = path.join(self.filePath, str(self.pokemon + ".csv"))
        print(self.csvFile)

        self.pokesql = sqldata.pokeData()
        self.database, self.cur = self.pokesql.databaseSetup()

        self.dataCheck()

    def webGet(self):
        rawHTML = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        testtable = pd.read_html(rawHTML.text, index_col = 0)

        #print(testtable[3])
        rawTable = testtable[3].rename(columns = {0 : 'Stat', 1 : 'Base', 3 : 'Min', 4 : 'Max'})
        print(rawTable)
        print(len(rawTable.columns))
        #testtable[3].to_csv(self.csvFile, index=None)
        if len(rawTable.columns) == 6:
            finalTable = rawTable.drop(rawTable.columns[[1, 4, 5]], axis = 1)
        if len(rawTable.columns) == 5:
            finalTable = rawTable.drop(rawTable.columns[[1, 4]], axis = 1)
        if len(rawTable.columns) < 5:
            finalTable = rawTable.drop(rawTable.columns[1], axis = 1)

        print(finalTable)
        print(len(finalTable.columns))
        finalTable.to_csv(self.csvFile)
        finalTable.to_sql(self.pokemon, self.database, if_exists="replace")
        sqlTest = pd.read_sql_query('SELECT * FROM %s' %self.pokemon, self.database)
        print(sqlTest)
        print("The above was a test pull from the SQL tables")
        
    def localGet(self):
        print('Attempting to grab local data.')
        pokeData = pd.read_csv(self.csvFile)
        print(pokeData)

    def dataCheck(self):
        testsql = self.cur.execute("SELECT count(*) from sqlite_master WHERE type='table' and name=?", (self.pokemon,))
        print (testsql)

        if  testsql == 1 and not self.force:
            print("Table was found in .db file")
        elif testsql == 1 and self.force:
            print("Table was found in .db file; Updating table from the web")
        elif testsql != 1:
            print("Table was not found; Searching web for data")

        self.cur.close()

        if path.exists(self.csvFile) and not self.force:
            print("Data already exists in the database for this Pokemon.")
            self.localGet()
        elif path.exists(self.csvFile) and self.force:
            print("Updating tables from web!")
            self.webGet()
        else:
            print(self.csvFile + " File Not Found!")
            self.webGet()

        self.pokesql.closeDatabase()
