import sqlite3
from sqlite3 import Error
from os import path

class pokeData:
    def databaseSetup(self):
        self.dbfile = path.join(".", "data", "pokemon.db")

        try:
            self.database = sqlite3.connect(self.dbfile)
            self.cur = self.database.cursor()
        except Error as e:
            print(e)
        finally:
            return(self.database, self.cur)

    def closeDatabase(self):
        self.cur.close()
        self.database.close()