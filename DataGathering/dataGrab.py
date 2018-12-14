import sys
from os import path
from bs4 import BeautifulSoup as soup
import pandas as pd
import requests
import data.pokeDatabase as sql_data

class Gather:
    def search_init(self, pokemon, force):
        self.pokemon = pokemon.lower()
        self.force = force
        self.file_path = path.join(".", "data")

        self.url = 'https://pokemondb.net/pokedex/' + self.pokemon
        self.csv_file = path.join(self.file_path, str(self.pokemon + ".csv"))
        print(self.csv_file)

        self.poke_sql = sql_data.pokeData()
        self.database, self.cur = self.poke_sql.database_setup()

        self.data_check()

    def web_get(self):
        raw_HTML = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        test_table = pd.read_html(raw_HTML.text, index_col = 0)

        #print(test_table[3])
        raw_table = test_table[3].rename(columns = {0 : 'Stat', 1 : 'Base', 3 : 'Min', 4 : 'Max'})
        #print(raw_table)
        #print(len(raw_table.columns))
        #test_table[3].to_csv(self.csvFile, index=None)
        if len(raw_table.columns) == 6:
            final_table = raw_table.drop(raw_table.columns[[1, 4, 5]], axis = 1)
        if len(raw_table.columns) == 5:
            final_table = raw_table.drop(raw_table.columns[[1, 4]], axis = 1)
        if len(raw_table.columns) < 5:
            final_table = raw_table.drop(raw_table.columns[1], axis = 1)

        #print(final_table)
        #print(len(final_table.columns))
        #final_table.to_csv(self.csv_file)
        self.cur.close()
        final_table.to_sql(self.pokemon, self.database, if_exists="replace")
        pokemon_sql_table = pd.read_sql_query('SELECT * FROM %s' %self.pokemon, self.database)
        print(pokemon_sql_table)
        #print("The above was a test pull from the SQL tables")
        return (pokemon_sql_table)
        
    def local_get(self):
        print('Attempting to grab local data.')
        #pokeData = pd.read_csv(self.csvFile)
        pokemon_sql_table = pd.read_sql_query('SELECT * FROM %s' %self.pokemon, self.database)
        #print(pokeData)
        print(pokemon_sql_table)
        return(pokemon_sql_table)

    def create_table_for_window(self, pandas_poke_table):
        pass

    def data_check(self):
        testsql = self.cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' and name=?", (self.pokemon,)).fetchone()[0]
        print (self.cur.fetchone())
        print (testsql)

        if testsql == 1 and not self.force:
            print("Table was found in .db file")
            self.local_get()
        elif testsql == 1 and self.force:
            print("Table was found in .db file; Updating table from the web")
            self.web_get()
        elif testsql != 1:
            print("Table was not found; Searching web for data")
            self.web_get()

        self.poke_sql.close_database()
